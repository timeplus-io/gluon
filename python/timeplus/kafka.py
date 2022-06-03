"""
kafka

This module defines kafka sink and source class  
:copyright: (c) 2022 by Timeplus  
:license: Apache2, see LICENSE for more details.  
"""


from timeplus.base import Base
from timeplus.source import Source
from timeplus.sink import Sink


class KafkaProperties(Base):
    """
    KafkaProperties class defines kafka source properties.
    """

    def __init__(self):
        Base.__init__(self)
        self.prop("data_type", "json")

    def topic(self, *args):
        return self.prop("topic", *args)

    def brokers(self, *args):
        return self.prop("brokers", *args)

    def data_type(self, *args):
        return self.prop("data_type", *args)

    # none, plain or scram
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

    def disable_tls(self):
        return self.prop("tls", {"disable": True, "skip_verify_server": True})


class KafkaSource(Source):
    """
    KafkaSource class defines kafka source.
    """

    def __init__(self, env=None):
        Source.__init__(self, env)
        self.type("kafka")


class KafkaSink(Sink):
    """
    KafkaSink class defines kafka sink.
    """

    def __init__(self):
        Sink.__init__(self)
        self.type("kafka")
