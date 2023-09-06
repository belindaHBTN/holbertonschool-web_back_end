#!/usr/bin/env python3
"""Helper function that takes page and page_size and return tuple"""
import csv
import math
from typing import List


def index_range(page, page_size):
    """return a tuple"""
    if page < 1 or page_size < 1:
        return None

    start_index = (page - 1) * page_size
    end_index = page * page_size

    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """return the appropriate page of the dataset"""
        assert isinstance(page, int) and isinstance(page_size, int), "bad arg"
        assert page > 0 and page_size > 0, "bad arg"

        if (page * page_size) > len(self.__dataset):
            return []
        index_range = index_range(page, page_size)
        data_list = []
        for row in index_range:
            data_list.append(row)
        return data_list
