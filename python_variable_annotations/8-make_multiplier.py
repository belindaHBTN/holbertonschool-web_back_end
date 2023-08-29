#!/usr/bin/env python3
"""a type-annotations function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable([float],float):
    """return a function that multiplies a float by multiplier"""
    def multiple_func(n: float) -> float:
        """multiple function"""
        return n * multiplier
    return multiple_func
