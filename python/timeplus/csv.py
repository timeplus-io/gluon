"""
csv

This module defines csv source  
:copyright: (c) 2022 by Timeplus  
:license: Apache2, see LICENSE for more details.  
"""

from timeplus.base import Base
from timeplus.source import Source


class CSVProperties(Base):
    """
    CSV properties
    """

    def __init__(self):
        Base.__init__(self)
        self.prop("type", "csv")

    def path(self, *args):
        return self.prop("path", *args)


class CSVSource(Source):
    """
    CSV Source class
    """

    def __init__(self, env=None):
        Source.__init__(self, env)
        self.type("file")
        self._properties = CSVProperties()
        self.properties(self._properties)

    def path(self, path):
        self._properties.path(path)
        self.properties(self._properties)
        return self
