#!/usr/bin/env python3
"""a type-annotations function"""
from typing import TypeVar, Dict


K = TypeVar('K')
T = TypeVar('V')


def safely_get_value(dct: Dict[K, V], key: K, default: V = None) -> V:
    """return lst or None"""
    if key in dct:
        return dct[key]
    else:
        return default
