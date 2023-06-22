"""
error
This module defines error class
:copyright: (c) 2022 by Timeplus
:license: Apache2, see LICENSE for more details.
"""

from sqlalchemy.exc import CompileError


class TimeplusAPIError(Exception):
    """Exception raised for errors in the timeplus api.
    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="failed to call timeplus API"):
        self.message = message
        super().__init__(self.message)


class Error(Exception):
    pass


class Warning(Exception):
    pass


class InterfaceError(Error):
    pass


class DatabaseError(Error):
    pass


class InternalError(DatabaseError):
    pass


class OperationalError(DatabaseError):
    pass


class ProgrammingError(DatabaseError):
    pass


class IntegrityError(DatabaseError):
    pass


class DataError(DatabaseError):
    pass


class NotSupportedError(CompileError):
    pass
