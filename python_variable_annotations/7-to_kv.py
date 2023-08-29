#!/usr/bin/env python3
"""a type-annotations function"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """display a string and a calculation result"""
    return (k, float(v**2))
