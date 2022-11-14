from pprint import pprint
import time
import dateutil.parser

import sseclient
from websocket import create_connection, WebSocketConnectionClosedException

from .type import Type

import rx
import json

import traceback


class QueryStreamV1:
    def __init__(self, configuration, response):
        self._configuration = configuration
        self._response = response

        # TODO: this is a buggy way to parse url, need to switch to robust parsing later
        self._ws_url = (
            self._configuration.host.replace("http", "ws").replace("api", "ws/queries/")
            + self._response._id
        )
        self.stopped = False

    def header(self):
        return self._response.result.header

    # TODO : implement auto delete function
    def _delete(self):
        pass

    def stop(self, delete=True):
        self.stopped = True
        if delete:
            self._delete()

    def show_query_result(self, count=10):
        ws = create_connection(
            self._ws_url,
            header=[f'X-Api-Key: {self._configuration.api_key["X-Api-Key"]}'],
        )

        for i in range(count):
            try:
                result = ws.recv()
                pprint(result)
            except WebSocketConnectionClosedException:
                break

    # TODO: refactor this complex method
    def _query_op(self, timeout=0):  # noqa: C901
        def __query_op(observer, scheduler):
            ws = create_connection(
                self._ws_url,
                header=[f'X-Api-Key: {self._configuration.api_key["X-Api-Key"]}'],
            )

            start_time = time.time()
            try:
                while True:
                    now = time.time()
                    if timeout != 0 and now - start_time > timeout:
                        break

                    if self.stopped:
                        break
                    result = ws.recv()
                    # convert string object to json(array)
                    # todo convert by header type
                    try:
                        record = json.loads(result)
                    except Exception as e:
                        pprint(f"cannot load result from ws {result} {e}")
                        continue

                    for index, col in enumerate(self.header()):
                        if col.type.startswith(Type.Tuple.value):
                            record[index] = tuple(record[index])
                        elif col.type.startswith(Type.Date.value):
                            try:
                                record[index] = dateutil.parser.isoparse(record[index])
                            except Exception as e:
                                pprint("failed to parse datetime ", e)

                    observer.on_next(record)
                observer.on_complete()
            except WebSocketConnectionClosedException:
                observer.on_complete()
            except Exception as e:
                pprint("failed to recieve data from websocket", e)
                observer.on_error(e)

        return __query_op

    def get_result_stream(self, timeout=0):
        strem_query_ob = rx.create(self._query_op(timeout=timeout))
        return strem_query_ob


class QueryStreamV2:
    def __init__(self, response):
        self._response = response
        self._sse_client = sseclient.SSEClient(self._response)

    def events(self):
        return self._sse_client.events()
