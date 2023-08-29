#!/usr/bin/env python3
"""a type-annotations function"""
from typing import TypeVar, Dict, Any, Union


T = TypeVar('T')


def safely_get_value(dct: Dict[Any, T], key: Any, default: T = None) -> T:
    """return lst or None"""
    if key in dct:
        return dct[key]
    else:
        return default
