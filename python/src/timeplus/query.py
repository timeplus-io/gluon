import requests
import json
from websocket import create_connection
import rx
import dateutil.parser

from timeplus.resource import ResourceBase
from timeplus.env import Env
from timeplus.type import Type


class Query(ResourceBase):
    _resource_name = "queries"

    def __init__(self, env=None):
        ResourceBase.__init__(self, env)

    @classmethod
    def build(cls, query, env=None):
        obj = cls(env=env)
        obj._data = query
        return obj

    @classmethod
    def execSQL(cls, sql, timeout=10, env=None):
        url = f"{cls._base_url}/sql"
        env.logger().debug(f"post {url}")
        sqlRequest = {"sql": sql, "timeout": timeout}

        if env is None:
            env = Env.current()

        cls._headers["Authorization"] = f"Bearer {env.access_token()}"
        cls._base_url = env.base_url()

        try:
            r = requests.post(f"{url}", json=sqlRequest, headers=cls._headers)
            if r.status_code < 200 or r.status_code > 299:
                env.logger.error(f"failed to run sql {r.status_code} {r.text}")
            else:
                return r.json()
        except Exception as e:
            env.logger.error(f"failed to run sql {e}")

    @classmethod
    def exec(cls, sql, env=None):
        url = f"{cls._base_url}/exec"
        env.logger.debug(f"post {url}")
        sqlRequest = {
            "sql": sql,
        }

        if env is None:
            env = Env.current()
        cls._headers["Authorization"] = f"Bearer {env.access_token()}"
        cls._base_url = env.base_url()

        try:
            r = requests.post(f"{url}", json=sqlRequest, headers=cls._headers)
            if r.status_code < 200 or r.status_code > 299:
                env.logger.error(f"failed to run exec {r.status_code} {r.text}")
            else:
                return r.json()
        except Exception as e:
            env.logger.error(f"failed to run exec {e}")

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

    def header(self):
        self.get()
        return self.prop("result")["header"]

    def cancel(self):
        self.action("cancel")
        return self

    def sink_to(self, sink):
        url = f"{self._base_url}/{self._resource_name}/{self.id()}/sinks"
        self._logger.debug(f"post {url}")
        sinkRequest = {"sink_id": sink.id()}

        try:
            r = requests.post(f"{url}", json=sinkRequest, headers=self._headers)
            if r.status_code < 200 or r.status_code > 299:
                self._logger.error(
                    f"failed to add sink {sink.id()} to query {self.id()} {r.status_code} {r.text}"
                )
            else:
                self._logger.debug(f"add sink {sink.id()} to query {self.id()} success")
        except Exception as e:
            self._logger.error(f"failed to add sink {e}")
        finally:
            return self

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
    def _query_op(self, stopper):  # noqa: C901
        def __query_op(observer, scheduler):
            # TODO : use WebSocketApp
            ws_schema = "ws"
            if self._env.schema() == "https":
                ws_schema = "wss"
            ws = create_connection(
                f"{ws_schema}://{self._env.host()}:{self._env.port()}/ws/queries/{self.id()}"
            )
            try:
                while True:
                    if stopper.is_stopped():
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

    def get_result_stream(self, stopper):
        strem_query_ob = rx.create(self._query_op(stopper))
        return strem_query_ob


class Stopper:
    def __init__(self):
        self.stopped = False

    def stop(self):
        self.stopped = True

    def is_stopped(self):
        return self.stopped
