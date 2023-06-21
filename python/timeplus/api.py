import json
import itertools
from collections import namedtuple

from timeplus import Environment, Query, Stream
from timeplus.error import Error


def connect(
    host="localhost",
    port=443,
    scheme="https",
    path="",
    user=None,
    password=None,
    context=None,
    header=False,
    ssl_verify_cert=True,
    ssl_client_cert=None,
    proxies=None,
):
    address = f"{scheme}://{host}:{port}"
    apikey = password
    workspace = path
    return Connection(address, apikey, workspace)


class Connection(object):
    """Connection to a Timeplus workspace."""

    def __init__(
        self, address="https://us.timeplus.cloud", apikey=None, workspace=None
    ):
        self.env = Environment().address(address).workspace(workspace).apikey(apikey)
        self.closed = False
        self.cursors = []

    def close(self):
        """Close the connection now."""
        self.closed = True
        for cursor in self.cursors:
            try:
                cursor.close()
            except Error:
                pass  # already closed

    def commit(self):
        # no commit support
        pass

    def rollback(self):
        # no rollback support
        pass

    def cursor(self):
        """Return a new Cursor Object using the connection."""

        cursor = Cursor(self.env)
        self.cursors.append(cursor)  # when to delete older cursor?

        return cursor

    def execute(self, operation, parameters=None):
        cursor = self.cursor()
        return cursor.execute(operation, parameters)

    def __enter__(self):
        return self.cursor()

    def __exit__(self, *exc):
        self.close()

    # internal method in a hacky way,
    # since some SQL is not exposed through API yet
    def _exist(self, name):
        stream = Stream(env=self.env).name(name)
        return stream.exist()

    def _get_table(self, name):
        stream = Stream(env=self.env).name(name).get()
        return stream


class Cursor(object):
    """Connection Cursor"""

    def __init__(self, env):
        self.env = env
        self.closed = False
        self.description = []
        self._results = None
        self._is_streaming = None
        self.query = None
        self.header = None

    # refer to https://peps.python.org/pep-0249/#description
    def description(self):
        return self.description

    @property
    def rowcount(self):
        return -1

    def close(self):
        """Close the cursor."""
        try:
            if self.query is not None:
                self.query.cancel()
        finally:
            self.closed = True

    def execute(self, operation, parameters=None):
        sql = apply_parameters(operation, parameters)
        analyze_result = Query(env=self.env).sql(query=sql).analyze()

        self._is_streaming = analyze_result.is_streaming
        self._query_type = analyze_result.query_type

        if self._query_type != "SELECT":
            raise Error("only select query is supported now")

        self._results = self._stream_query(sql)
        return self

    def executemany(self, operation, seq_of_parameters=None):
        raise Error("`executemany` is not supported")

    def fetchone(self):
        """
        Fetch the next row of a query result set, returning a single sequence,
        or `None` when no more data is available.
        """
        try:
            return self.next()
        except StopIteration:
            return None

    def fetchmany(self, size=None):
        """
        Fetch the next set of rows of a query result, returning a sequence of
        sequences (e.g. a list of tuples). An empty sequence is returned when
        no more rows are available.
        """
        size = size or self.arraysize
        return list(itertools.islice(self._results, size))

    def fetchall(self):
        """
        Fetch all (remaining) rows of a query result, returning them as a
        sequence of sequences (e.g. a list of tuples). Note that the cursor's
        arraysize attribute can affect the performance of this operation.
        """
        return list(self._results)

    def setinputsizes(self, sizes):
        # not supported
        pass

    def setoutputsizes(self, sizes):
        # not supported
        pass

    def __iter__(self):
        return self

    def __next__(self):
        return next(self._results)

    next = __next__

    def _stream_query(self, query):
        self.query = Query(env=self.env).sql(query=query).create()
        self.header = self.query.header()
        field_names = [field["name"] for field in self.header]
        keys = " ".join(field_names)

        self.description = [
            (
                field["name"],  # name
                field["type"],  # type
                None,  # [display_size]
                None,  # [internal_size]
                None,  # [precision]
                None,  # [scale]
                False,  # [null_ok]
            )
            for field in self.header
        ]

        for event in self.query.result():
            if event.event == "message":
                data = json.loads(event.data)
                for row in data:
                    Row = namedtuple(
                        "Row", keys, rename=True
                    )  # _tp_time will be renamed here
                    yield Row(*row)


def apply_parameters(operation, parameters):
    if not parameters:
        return operation

    escaped_parameters = {key: escape(value) for key, value in parameters.items()}
    return operation % escaped_parameters


def escape(value):
    if value == "*":
        return value
    elif isinstance(value, str):
        return "'{}'".format(value.replace("'", "''"))
    elif isinstance(value, bool):
        return "TRUE" if value else "FALSE"
    elif isinstance(value, (int, float)):
        return value
    elif isinstance(value, (list, tuple)):
        return ", ".join(escape(element) for element in value)
