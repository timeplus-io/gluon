"""
query

This module defines query class  
:copyright: (c) 2022 by Timeplus  
:license: Apache2, see LICENSE for more details.  
"""

import json
import time
from websocket import create_connection
import rx
import dateutil.parser

from timeplus.resource import ResourceBase
from timeplus.env import Env
from timeplus.type import Type
from timeplus.error import TimeplusAPIError, TimeplusQueryError


class Query(ResourceBase):
    """
    Query class defines query object.
    """

    _resource_name = "queries"

    def __init__(self, env=None):
        ResourceBase.__init__(self, env)
        self.stopped = False

    @classmethod
    def build(cls, query, env=None):
        obj = cls(env=env)
        obj._data = query
        return obj

    @classmethod
    def execSQL(cls, sql, timeout=0, env=None):
        if env is None:
            env = Env.current()
        query = Query().name("unamed").sql(sql)
        query.create()

        if query.status() == "failed":
            raise TimeplusQueryError(query.message())

        result = {}
        result["header"] = query.header()
        result["data"] = []
        query.get_result_stream(timeout=timeout).subscribe(
            on_next=lambda i: result["data"].append(i),
            on_error=lambda e: print(f"error {e}"),  # todo better handling this error
            on_completed=lambda: query.stop(),
        )

        return result

    def name(self, *args):
        return self.prop("name", *args)

    def description(self, *args):
        return self.prop("description", *args)

    def sql(self, *args):
        return self.prop("sql", *args)

    def tags(self, *args):
        return self.prop("tags", *args)

    def id(self):
        return self.prop("id")

    def stat(self):
        self.get()
        return self.prop("stat")

    def status(self):
        self.get()
        return self.prop("status")

    def message(self):
        self.get()
        return self.prop("message")

    def header(self):
        self.get()
        return self.prop("result")["header"]

    def cancel(self):
        self.action("cancel")
        return self

    def stop(self):
        self.stopped = True

    def sink_to(self, sink):
        url = f"{self._base_url}/{self._resource_name}/{self.id()}/sinks"
        self._logger.debug(f"post {url}")
        sinkRequest = {"sink_id": sink.id()}

        try:
            self._env.http_post(url, sinkRequest)
            return self
        except Exception as e:
            raise e

    def show_query_result(self, count=10):
        ws_schema = "ws"
        if self._env.schema() == "https":
            ws_schema = "wss"
        ws = create_connection(
            f"{ws_schema}://{self._env.host()}:{self._env.port()}/ws/queries/{self.id()}"
        )
        for i in range(count):
            result = ws.recv()
            self._logger.info(result)

    # TODO: refactor this complex method
    def _query_op(self, timeout=0):  # noqa: C901
        def __query_op(observer, scheduler):
            # TODO : use WebSocketApp
            ws_schema = "ws"
            if self._env.schema() == "https":
                ws_schema = "wss"
            ws = create_connection(
                f"{ws_schema}://{self._env.host()}:{self._env.port()}/ws/queries/{self.id()}"
            )
            start_time = time.time()
            try:
                while True:
                    now = time.time()
                    if timeout != 0 and now - start_time > timeout:
                        self._logger.debug("query timeout")
                        break

                    if self.stopped:
                        break
                    result = ws.recv()
                    # convert string object to json(array)
                    # todo convert by header type
                    record = json.loads(result)

                    for index, col in enumerate(self.header()):
                        if col["type"].startswith(Type.Tuple.value):
                            record[index] = tuple(record[index])
                        elif col["type"].startswith(Type.Date.value):
                            try:
                                record[index] = dateutil.parser.isoparse(record[index])
                            except Exception as e:
                                self._logger.error("failed to parse datetime ", e)

                    observer.on_next(record)
                observer.on_complete()
            except Exception:
                pass

        return __query_op

    def get_result_stream(self, timeout=0):
        strem_query_ob = rx.create(self._query_op(timeout=timeout))
        return strem_query_ob
