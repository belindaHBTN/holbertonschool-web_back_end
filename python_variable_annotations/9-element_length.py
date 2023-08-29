#!/usr/bin/env python3
"""a type-annotations function"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """count the number of elements"""
    return [(i, len(i)) for i in lst]
