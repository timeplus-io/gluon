import multiprocessing
import os

import requests
from requests.structures import CaseInsensitiveDict
from websocket import create_connection

import rx
from rx.scheduler import ThreadPoolScheduler
from rx import operators as ops

SCHEMA = os.getenv("TIMEPLUS_SCHEMA", "http")
NEUTRON_SERVER = os.getenv("NEUTRON_HOST", "localhost")
NEUTRON_PORT = os.getenv("NEUTRON_PORT", "8000")


class Base:
    def __init__(self):
        self._data = {}

    def prop(self, name, *args):
        if len(args) == 0:
            return self._get(name)
        elif len(args) == 1:
            return self._set(name, args[0])
        else:
            raise Exception("invalid number of arguments")

    def _set(self, key, value):
        if isinstance(value, Base):
            self._data[key] = value.data()
        else:
            self._data[key] = value
        return self

    def _get(self, key):
        return self._data[key]

    def data(self):
        return self._data

    def id(self):
        return self._get("id")


class Env(Base):
    def __init__(self):
        Base.__init__(self)
        self.host("localhost")
        self.port("8000")
        self.schema("http")

        self.auth0_domain = "timeplus.us.auth0.com"
        self.audience = "https://timeplus.us.auth0.com/api/v2/"
        self.grant_type = "client_credentials"

        self._headers = CaseInsensitiveDict()
        self._headers["Accept"] = "application/json"
        self._headers["Content-Type"] = "application/json"

    def host(self, *args):
        return self.prop("host", *args)

    def port(self, *args):
        return self.prop("port", *args)

    def schema(self, *args):
        return self.prop("schema", *args)

    def base_url(self):
        return f"{self.schema()}://{self.host()}:{self.port()}/api/v1beta1"

    def headers(self):
        self._headers["Authorization"] = f"Bearer {self.access_token()}"
        return self._headers

    def token(self, *args):
        return self.prop("token", *args)

    def access_token(self, *args):
        if "token" in self._data:
            return self._data["token"]["access_token"]
        return ""

    def login(
        self,
        client_id="Ed3T1s33G4CaLIZdZSrzccCuM5nklz2G",
        client_secret="UdhOkap9ZqQjLvmuCRTf1w_T6TcoHL4RYCxuv3EWxNfnoVp8Dpu_udMQi5rGX5Ce",
    ):
        url = f"https://{self.auth0_domain}/oauth/token"
        print(f"post {url}")
        request_data = {
            "client_id": client_id,
            "client_secret": client_secret,
            "audience": self.audience,
            "grant_type": self.grant_type,
        }
        headers = {"Content-Type": "application/json"}
        try:
            r = requests.post(
                url,
                json=request_data,
                headers=headers,
            )
            if r.status_code < 200 or r.status_code > 299:
                print(f"failed to login {r.status_code } {r.text}")
                raise Exception(f"failed to login {r.status_code } {r.text}")
            else:
                print(f"token has been granted")
                self.token(r.json())
                return self
        except Exception as e:
            raise e

    def logout(self):
        self.token({})
        return self


class ResourceBase(Base):
    _resource_name = "resource"

    def __init__(self, env=None):
        Base.__init__(self)
        if env is None:
            env = Env()
        self._headers = env.headers()
        self._base_url = env.base_url()
        self._env = env
        print(f"init result with base url {self._base_url} header {self._headers}")

    def create(self):
        url = f"{self._base_url}/{self._resource_name}/"
        print(f"post {url} with header {self._headers}")
        try:
            r = requests.post(
                f"{self._base_url}/{self._resource_name}/",
                json=self.data(),
                headers=self._headers,
            )
            if r.status_code < 200 or r.status_code > 299:
                print(
                    f"failed to create {self._resource_name} {r.status_code } {r.text}"
                )
            else:
                print(f"source {self._resource_name} has been created")
                self._data = r.json()
        except Exception as e:
            print(f"failed to create {self._resource_name} {e}")
        finally:
            return self

    def get(self):
        print(f"get {self._base_url}/{self._resource_name}/")
        try:
            r = requests.get(
                f"{self._base_url}/{self._resource_name}/{self.id()}",
                headers=self._headers,
            )
            if r.status_code < 200 or r.status_code > 299:
                print(f"failed to get {self._resource_name} {r.text}")
            else:
                print(f"get {self._resource_name} success")
                self._data = r.json()
        except Exception as e:
            print(f"failed to get {self._resource_name} {e}")
        finally:
            return self

    def delete(self):
        print(f"delete {self._base_url}/{self._resource_name}/{self.id()}")
        try:
            r = requests.delete(
                f"{self._base_url}/{self._resource_name}/{self.id()}",
                headers=self._headers,
            )
            if r.status_code < 200 or r.status_code > 299:
                print(
                    f"failed to delete {self._resource_name} {r.status_code} {r.text}"
                )
            else:
                print(f"delete {self._resource_name} success")
        except Exception as e:
            print(f"failed to delete {self._resource_name} {e}")
        finally:
            return self

    def action(self, action_name):
        print(f"post {self._base_url}/{self._resource_name}/{self.id()}/{action_name}")
        try:
            r = requests.post(
                f"{self._base_url}/{self._resource_name}/{self.id()}/{action_name}",
                headers=self._headers,
            )
            if r.status_code < 200 or r.status_code > 299:
                print(f"failed to post {action_name} on {self._resource_name} {r.text}")
            else:
                print(f"{action_name} {self._resource_name} success")
        except Exception as e:
            print(f"failed to {action_name} {self._resource_name} {e}")
        finally:
            return self

    @classmethod
    def list(cls, env=None):
        if env is None:
            env = Env()
        headers = env.headers()
        base_url = env.base_url()

        try:
            url = f"{base_url}/{cls._resource_name}/"
            r = requests.get(url, headers=headers)
            if r.status_code < 200 or r.status_code > 299:
                print(f"failed to list {cls._resource_name} {r.text}")
            else:
                print(f"list {cls._resource_name} success")
                result = [cls.build(val, env=env) for val in r.json()]
                return result
        except Exception as e:
            print(f"failed to list {cls._resource_name}")


class SourceConnection(Base):
    def __init__(self):
        Base.__init__(self)
        self._set("auto_create", True)

    def stream(self, *args):
        return self.prop("stream_name", *args)

    def auto_create(self, *args):
        return self.prop("auto_create", *args)

    def event_time_column(self, *args):
        return self.prop("event_time_column", *args)


class Source(ResourceBase):
    _resource_name = "sources"

    def __init__(self, env=None):
        ResourceBase.__init__(self, env)

    @classmethod
    def build(cls, id, env=None):
        obj = cls(env=env)
        obj._set("id", id)
        return obj

    def name(self, *args):
        return self.prop("name", *args)

    def connection(self, *args):
        try:
            return self.prop("connection_config", *args)
        except:
            # TODO it is better to change connection_config to connection here
            return self.prop("connection", *args)

    def properties(self, *args):
        return self.prop("properties", *args)

    def type(self, *args):
        return self.prop("type", *args)

    def id(self):
        return self.prop("id")

    def stat(self):
        self.get()
        return self.connection()["stat"]

    def start(self):
        self.action("start")
        return self

    def stop(self):
        self.action("stop")
        return self

    def preview(self, size=3):
        url = f"{self._base_url}/source/preview"
        print(f"post {url}")
        previewRequest = {
            "properties": self.properties(),
            "size": size,
            "type": self.type(),
        }

        try:
            r = requests.post(f"{url}", json=previewRequest, headers=self._headers)
            if r.status_code < 200 or r.status_code > 299:
                print(f"failed to preview source {r.status_code} {r.text}")
            else:
                return r.json()
        except Exception as e:
            print(f"failed to preivew {e}")


# stream generator source
class GeneratorSource(Source):
    def __init__(self, env=None):
        Source.__init__(self, env)
        self.type("stream_generator")

    def config(self, configuration):
        properties = GeneratorProperties().configuration(configuration)
        self.properties(properties)
        return self


class GeneratorProperties(Base):
    def __init__(self):
        Base.__init__(self)

    def configuration(self, *args):
        return self.prop("configuration", *args)


class GeneratorConfiguration(Base):
    def __init__(self):
        Base.__init__(self)
        self._set("batch_size", 1)
        self._set("interval", 1000)

    def batch(self, *args):
        return self.prop("batch_size", *args)

    def interval(self, *args):
        return self.prop("interval", *args)

    def field(self, field_instance):
        if "fields" not in self._data:
            self._data["fields"] = []
        self._data["fields"].append(field_instance.data())

        return self


class GeneratorField(Base):
    def __init__(self):
        Base.__init__(self)

    def name(self, *args):
        return self.prop("name", *args)

    def type(self, *args):
        return self.prop("type", *args)

    def limit(self, *args):
        return self.prop("limit", *args)

    def timestamp_format(self, *args):
        return self.prop("timestamp_format", *args)


# csv source
class CSVProperties(Base):
    def __init__(self):
        Base.__init__(self)
        self.prop("type", "csv")

    def path(self, *args):
        return self.prop("path", *args)


class CSVSource(Source):
    def __init__(self, env=None):
        Source.__init__(self, env)
        self.type("file")
        self._properties = CSVProperties()
        self.properties(self._properties)

    def path(self, path):
        self._properties.path(path)
        self.properties(self._properties)
        return self


class KafkaProperties(Base):
    def __init__(self):
        Base.__init__(self)
        self.prop("data_type", "json")

    def topic(self, *args):
        return self.prop("topic", *args)

    def brokers(self, *args):
        return self.prop("brokers", *args)

    ## none, plain or scram
    def sasl(self, *args):
        return self.prop("sasl", *args)

    def username(self, *args):
        return self.prop("username", *args)

    def password(self, *args):
        return self.prop("password", *args)

    def group(self, *args):
        return self.prop("group", *args)

    # `latest` or `earlist`
    def offset(self, *args):
        return self.prop("offset", *args)

    def partition_number(self, *args):
        return self.prop("partition_number", *args)

    def replication_factor(self, *args):
        return self.prop("replication_factor", *args)


class KafkaSource(Source):
    def __init__(self, env=None):
        Source.__init__(self, env)
        self.type("kafka")


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
        print(f"post {url}")
        sqlRequest = {"sql": sql, "timeout": timeout}

        if env is None:
            env = Env()

        cls._headers["Authorization"] = f"Bearer {env.access_token()}"
        cls._base_url = env.base_url()

        try:
            r = requests.post(f"{url}", json=sqlRequest, headers=cls._headers)
            if r.status_code < 200 or r.status_code > 299:
                print(f"failed to run sql {r.status_code} {r.text}")
            else:
                return r.json()
        except Exception as e:
            print(f"failed to run sql {e}")

    @classmethod
    def exec(cls, sql, env=None):
        url = f"{cls._base_url}/exec"
        print(f"post {url}")
        sqlRequest = {
            "sql": sql,
        }

        if env is None:
            env = Env()
        cls._headers["Authorization"] = f"Bearer {env.access_token()}"
        cls._base_url = env.base_url()

        try:
            r = requests.post(f"{url}", json=sqlRequest, headers=cls._headers)
            if r.status_code < 200 or r.status_code > 299:
                print(f"failed to run exec {r.status_code} {r.text}")
            else:
                return r.json()
        except Exception as e:
            print(f"failed to run exec {e}")

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
        print(f"post {url}")
        sinkRequest = {"sink_id": sink.id()}

        try:
            r = requests.post(f"{url}", json=sinkRequest, headers=self._headers)
            if r.status_code < 200 or r.status_code > 299:
                print(
                    f"failed to add sink {sink.id()} to query {self.id()} {r.status_code} {r.text}"
                )
            else:
                print(f"add sink {sink.id()} to query {self.id()} success")
        except Exception as e:
            print(f"failed to add sink {e}")
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
            print(result)

    def _query_op(self, stopper):
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
                    observer.on_next(result)
                observer.on_complete()
            except Exception as e:
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


class Sink(ResourceBase):
    _resource_name = "sinks"

    def __init__(self, env=None):
        ResourceBase.__init__(self, env)

    @classmethod
    def build(cls, id, env=None):
        obj = cls(env=env)
        obj._set("id", id)
        return obj

    def name(self, *args):
        return self.prop("name", *args)

    def type(self, *args):
        return self.prop("type", *args)

    def properties(self, *args):
        return self.prop("properties", *args)


class KafkaSink(Sink):
    def __init__(self):
        Sink.__init__(self)
        self.type("kafka")


class SlackSink(Sink):
    def __init__(self):
        Sink.__init__(self)
        self.type("slack")


class SlackSinkProperty(Base):
    def __init__(self):
        Base.__init__(self)

    def url(self, *args):
        return self.prop("url", *args)

    def template(self, *args):
        return self.prop("name", *args)


class SMTPSink(Sink):
    def __init__(self):
        Sink.__init__(self)
        self.type("smtp")


class SMTPSinkProperty(Base):
    def __init__(self):
        Base.__init__(self)

    def f(self, *args):
        return self.prop("from", *args)

    def to(self, *args):
        return self.prop("to", *args)

    def username(self, *args):
        return self.prop("username", *args)

    def host(self, *args):
        return self.prop("host", *args)

    def port(self, *args):
        return self.prop("port", *args)

    def password(self, *args):
        return self.prop("password", *args)

    def template(self, *args):
        return self.prop("template", *args)


class StreamColumn(Base):
    def __init__(self):
        Base.__init__(self)

    def name(self, *args):
        return self.prop("name", *args)

    def type(self, *args):
        return self.prop("type", *args)

    def default(self, *args):
        return self.prop("default", *args)

    def compression_codec(self, *args):
        return self.prop("compression_codec", *args)

    def nullable(self, *args):
        return self.prop("nullable", *args)

    def skipping_index_expression(self, *args):
        return self.prop("skipping_index_expression", *args)

    def ttl_expression(self, *args):
        return self.prop("ttl_expression", *args)


class Stream(ResourceBase):
    _resource_name = "streams"

    def __init__(self, env=None):
        ResourceBase.__init__(self, env)
        self.prop("columns", [])

    @classmethod
    def build(cls, val, env=None):
        obj = cls(env=env)
        obj._data = val
        return obj

    ## the list api is not implemented, has to manually implement it here
    def get(self):
        print("in stream get")
        streams = Stream.list()
        for s in streams:
            if s.name() == self.name():
                return s

    def delete(self):
        print(f"delete {self._base_url}/{self._resource_name}/{self.name()}")
        try:
            r = requests.delete(
                f"{self._base_url}/{self._resource_name}/{self.name()}",
                headers=self._headers,
            )
            if r.status_code < 200 or r.status_code > 299:
                print(
                    f"failed to delete {self._resource_name} {r.status_code} {r.text}"
                )
            else:
                print(f"delete {self._resource_name} success")
        except Exception as e:
            print(f"failed to delete {self._resource_name} {e}")
        finally:
            return self

    def insert(self, data):
        url = f"{self._base_url}/{self._resource_name}/{self.name()}/ingest"
        print(f"post {url}")
        insertRequest = {"columns": self.columnNames(), "data": data}
        print(f"insert {insertRequest}")

        try:
            r = requests.post(f"{url}", json=insertRequest, headers=self._headers)
            if r.status_code < 200 or r.status_code > 299:
                print(f"failed to insert {r.status_code} {r.text}")
            else:
                print("insert success")
        except Exception as e:
            print(f"failed to insert {e}")
        finally:
            return self

    def name(self, *args):
        return self.prop("name", *args)

    def event_time_column(self, *args):
        return self.prop("event_time_column", *args)

    def order_by_expression(self, *args):
        return self.prop("order_by_expression", *args)

    def order_by_granularity(self, *args):
        return self.prop("order_by_granularity", *args)

    def partition_by_granularity(self, *args):
        return self.prop("partition_by_granularity", *args)

    def replication_factor(self, *args):
        return self.prop("replication_factor", *args)

    def shards(self, *args):
        return self.prop("shards", *args)

    def ttl_expression(self, *args):
        return self.prop("ttl_expression", *args)

    # note, no way to remove/rename col for now
    def column(self, col):
        col_prop = self.prop("columns")
        col_prop.append(col.data())
        self.prop("columns", col_prop)
        return self

    def columnNames(self):
        col_prop = self.prop("columns")
        return [x["name"] for x in col_prop if not x["name"].startswith("_tp")]
