#!/usr/bin/env python3
"""a type-annotations function"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sum of the elements in a list"""
    return sum(mxd_lst)
