#!/usr/bin/env python3
"""a type-annotations function"""
from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """return lst or None"""
    if lst:
        return lst[0]
    else:
        return None
