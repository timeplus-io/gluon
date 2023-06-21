import json
import sys
import itertools
from collections import namedtuple

from timeplus import Environment, Query
from timeplus.error import TimeplusAPIError


def connect(address="https://us.timeplus.cloud", apikey=None, workspace=None):
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
            except TimeplusAPIError:
                pass  # already closed

    def commit(self):
        # not commit support yet
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


class Cursor(object):
    """Connection Cursor"""

    def __init__(self, env):
        self.env = env
        self.closed = False
        self._results = None
        self._query = None
        self._header = None

    @property
    def rowcount(self):
        if not self._is_streaming:
            results = list(self._results)
            n = len(results)
            self._results = iter(results)
            return n
        else:
            # for streaming query no row count available
            return sys.maxsize

    def close(self):
        """Close the cursor."""
        try:
            if self.query is not None:
                self.query.cancel()
        finally:
            self.closed = True

    def execute(self, operation, parameters=None):
        # TODO: Run query analysis here
        # TODO: apply parameters here

        analyze_result = Query(env=self.env).sql(query=operation).analyze()

        self._is_streaming = analyze_result.is_streaming
        self._query_type = analyze_result.query_type

        if self._query_type != "SELECT":
            raise TimeplusAPIError("only select query is supported now")

        self._results = self._stream_query(operation)
        return self

    def executemany(self, operation, seq_of_parameters=None):
        raise TimeplusAPIError("`executemany` is not supported")

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
        self._header = self.query.header()
        field_names = [field["name"] for field in self._header]
        keys = " ".join(field_names)

        for event in self.query.result():
            if event.event == "message":
                data = json.loads(event.data)
                for row in data:
                    Row = namedtuple(
                        "Row", keys, rename=True
                    )  # _tp_time will be renamed here
                    yield Row(*row)
