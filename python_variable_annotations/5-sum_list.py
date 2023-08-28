#!/usr/bin/env python3
"""a type-annotations function"""


def sum_list(input_list: list[float]) -> float:
    """sum of the floats in a list"""
    sum: float = 0
    for el in input_list:
        sum += el
    return sum
