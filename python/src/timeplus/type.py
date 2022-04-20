"""
type

This module defines timeplust suppported data types
:copyright: (c) 2022 by Timeplus
:license: Apache2, see LICENSE for more details.
"""

from enum import Enum


class Type(Enum):
    """
    Type class is a enumeration that defines all the types supported by timeplus
    """

    Integer = "integer"
    Decimal = "decimal"
    Float = "float"
    Bool = "bool"
    String = "string"
    Date = "date"
    Datetime = "datetime"
    Datetime64 = "datetime64"
    Array = "array"
    Map = "map"
    Tuple = "tuple"
