import json
import re
import itertools
from collections import namedtuple

from timeplus import Environment, Query, Stream, View
from timeplus.error import Error


def check_closed(f):
    """Decorator that checks if connection/cursor is closed."""

    def wrap(self, *args, **kwargs):
        if self.closed:
            raise Error(
                "{klass} already closed".format(klass=self.__class__.__name__)
            )
        return f(self, *args, **kwargs)

    return wrap


def check_result(f):
    """Decorator that checks if the cursor has results from `execute`."""

    def wrap(self, *args, **kwargs):
        if self._results is None:
            raise Error("Called before `execute`")
        return f(self, *args, **kwargs)

    return wrap


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

    @check_closed
    def close(self):
        """Close the connection now."""
        self.closed = True
        for cursor in self.cursors:
            try:
                cursor.close()
            except Error:
                pass  # already closed

    @check_closed
    def commit(self):
        # no commit support
        pass

    @check_closed
    def rollback(self):
        # no rollback support
        pass

    @check_closed
    def cursor(self):
        """Return a new Cursor Object using the connection."""

        cursor = Cursor(self.env)
        self.cursors.append(cursor)  # when to delete older cursor?

        return cursor

    @check_closed
    def execute(self, operation, parameters=None):
        cursor = self.cursor()
        return cursor.execute(operation, parameters)

    def __enter__(self):
        return self.cursor()

    def __exit__(self, *exc):
        self.close()

    # internal method in a hacky way,
    # since some SQL is not exposed through API yet
    def _exist_table(self, name):
        stream = Stream(env=self.env).name(name)
        return stream.exist()

    def _exist_view(self, name):
        view = View(env=self.env).name(name)
        return view.exist()

    def _get_table(self, name):
        return Stream(env=self.env).name(name).get()

    def _get_view(self, name):
        return View(env=self.env).name(name).get()

    def _list_table(self):
        return Stream(env=self.env).list()

    def _list_view(self):
        return View(env=self.env).list()


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

        self.arraysize = 1

    # # refer to https://peps.python.org/pep-0249/#description
    # def description(self):
    #     return self.description

    @property
    @check_result
    @check_closed
    def rowcount(self):
        # consume the iterator
        results = list(self._results)
        n = len(results)
        self._results = iter(results)
        return n

    @check_closed
    def close(self):
        """Close the cursor."""
        try:
            if self.query is not None:
                self.query.cancel()
        finally:
            self.closed = True

    @check_closed
    def execute(self, operation, parameters=None):
        sql = apply_parameters(operation, parameters)
        analyze_result = Query(env=self.env).sql(query=sql).analyze()

        self._is_streaming = analyze_result.is_streaming
        self._query_type = analyze_result.query_type

        if self._query_type != "SELECT":
            raise Error("only select query is supported now")

        self._run_stream_query(sql)
        self._results = self._stream_query_iter()
        return self

    @check_closed
    def executemany(self, operation, seq_of_parameters=None):
        raise Error("`executemany` is not supported")

    @check_closed
    @check_result
    def fetchone(self):
        """
        Fetch the next row of a query result set, returning a single sequence,
        or `None` when no more data is available.
        """
        try:
            return self.next()
        except StopIteration:
            return None

    @check_result
    @check_closed
    def fetchmany(self, size=None):
        """
        Fetch the next set of rows of a query result, returning a sequence of
        sequences (e.g. a list of tuples). An empty sequence is returned when
        no more rows are available.
        """
        size = size or self.arraysize
        return list(itertools.islice(self._results, size))

    @check_result
    @check_closed
    def fetchall(self):
        """
        Fetch all (remaining) rows of a query result, returning them as a
        sequence of sequences (e.g. a list of tuples). Note that the cursor's
        arraysize attribute can affect the performance of this operation.
        """
        return list(self._results)

    @check_closed
    def setinputsizes(self, sizes):
        # not supported
        pass

    @check_closed
    def setoutputsizes(self, sizes):
        # not supported
        pass

    @check_closed
    def __iter__(self):
        return self

    @check_closed
    def __next__(self):
        return next(self._results)

    next = __next__

    def _run_stream_query(self, query):
        self.query = Query(env=self.env).sql(query=query).create()
        self.header = self.query.header()
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
        return

    def _stream_query_iter(self):
        field_names = [re.sub(r'[^a-zA-Z0-9]', '', field["name"]) for field in self.header]
        keys = " ".join(field_names)
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

    escaped_parameters = {key: escape(value)
                          for key, value in parameters.items()}
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
