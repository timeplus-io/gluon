"""
view

This module defines view class
:copyright: (c) 2022 by Timeplus
:license: Apache2, see LICENSE for more details.
"""


from timeplus.resource import ResourceBase


class View(ResourceBase):
    """
    View class defines base class for view
    """

    _resource_name = "views"

    def __init__(self, env=None):
        ResourceBase.__init__(self, env)

    @classmethod
    def build(cls, sink, env=None):
        obj = cls(env=env)
        obj._data = sink
        return obj

    def name(self, *args):
        return self.prop("name", *args)

    def query(self, *args):
        return self.prop("query", *args)

    def materialized(self, *args):
        return self.prop("materialized", *args)

    # the list api is not implemented, has to manually implement it here
    def get(self):
        views = View.list()
        for v in views:
            if v.name() == self.name():
                return v

    def delete(self):
        url = f"{self._base_url}/{self._resource_name}/{self.name()}"
        self._logger.debug("delete {}", url)

        try:
            self._env.http_delete(url)
            return self
        except Exception as e:
            raise e
