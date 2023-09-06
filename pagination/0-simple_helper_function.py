#!/usr/bin/env python3
"""Helper function that takes page and page_size and return tuple"""

def index_range(page, page_size):
    """return a tuple"""
    if page < 1 or page_size < 1:
        return None
    
    start_index = (page-1) * page_size
    end_index = page * page_size

    return (start_index, end_index)

