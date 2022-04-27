"""
slack

This module defines slack sink class  
:copyright: (c) 2022 by Timeplus  
:license: Apache2, see LICENSE for more details.  
"""

from timeplus.sink import Sink
from timeplus.base import Base


class SlackSink(Sink):
    """
    SlackSink class defines slack sink
    """

    def __init__(self):
        Sink.__init__(self)
        self.type("slack")


class SlackSinkProperty(Base):
    """
    SlackSinkProperty class defines slack sink property
    """

    def __init__(self):
        Base.__init__(self)

    def url(self, *args):
        return self.prop("url", *args)

    def message(self, *args):
        return self.prop("template", *args)
