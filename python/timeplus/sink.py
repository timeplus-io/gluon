"""
sink

This module defines sink class  
:copyright: (c) 2022 by Timeplus  
:license: Apache2, see LICENSE for more details.  
"""


from timeplus.resource import ResourceBase


class Sink(ResourceBase):
    """
    Sink class defines base class for sinks
    """

    _resource_name = "sinks"

    def __init__(self, env=None):
        ResourceBase.__init__(self, env)

    @classmethod
    def build(cls, sink, env=None):
        obj = cls(env=env)
        obj._data = sink
        return obj

    def name(self, *args):
        return self.prop("name", *args)

    def id(self):
        return self.prop("id")

    def type(self, *args):
        return self.prop("type", *args)

    def properties(self, *args):
        return self.prop("properties", *args)
