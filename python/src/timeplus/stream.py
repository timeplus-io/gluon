import requests

from timeplus.base import Base
from timeplus.resource import ResourceBase


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
