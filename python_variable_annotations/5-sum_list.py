#!/usr/bin/env python3
"""a type-annotations function"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """sum of the floats in a list"""
    return sum(input_list)
