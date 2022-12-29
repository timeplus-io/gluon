"""
error
This module defines error class
:copyright: (c) 2022 by Timeplus
:license: Apache2, see LICENSE for more details.
"""


class TimeplusAPIError(Exception):
    """Exception raised for errors in the timeplus api.
    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="failed to call timeplus API"):
        self.message = message
        super().__init__(self.message)
