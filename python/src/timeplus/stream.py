import requests
import json
from datetime import datetime

from timeplus.base import Base
from timeplus.resource import ResourceBase


class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        return json.JSONEncoder.default(self, o)


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

    # the list api is not implemented, has to manually implement it here
    def get(self):
        streams = Stream.list()
        for s in streams:
            if s.name() == self.name():
                return s

    def delete(self):
        url = f"{self._base_url}/{self._resource_name}/{self.name()}"
        self._logger.debug("delete {}", url)
        try:
            r = requests.delete(
                url,
                headers=self._headers,
                timeout=self._env.http_timeout(),
            )
            if r.status_code < 200 or r.status_code > 299:
                self._logger.error(
                    f"failed to delete {self._resource_name} {r.status_code} {r.text}"
                )
            else:
                self._logger.debug(f"delete {self._resource_name} success")
        except Exception as e:
            self._logger.error(f"failed to delete {self._resource_name} {e}")
        finally:
            return self

    def insert(self, data, headers=None):
        url = f"{self._base_url}/{self._resource_name}/{self.name()}/ingest"
        self._logger.debug("post {}", url)

        insert_headers = self.columnNames()
        if headers is not None:
            insert_headers = headers

        insertRequest = {
            "columns": insert_headers,
            "data": data,
        }
        self._logger.debug(f"insert {insertRequest}")

        try:
            self._logger.debug(
                f"insert {json.dumps(insertRequest, cls=DateTimeEncoder)}"
            )
            r = requests.post(
                url,
                data=json.dumps(insertRequest, cls=DateTimeEncoder),
                headers=self._headers,
                timeout=self._env.http_timeout(),
            )
            if r.status_code < 200 or r.status_code > 299:
                self._logger.error(f"failed to insert {r.status_code} {r.text}")
            else:
                self._logger.debug("insert success")
        except Exception as e:
            self._logger.error(f"failed to insert {e}")
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
