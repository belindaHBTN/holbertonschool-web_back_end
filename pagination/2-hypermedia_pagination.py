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

        dataset = self.dataset()
        if (page * page_size) > len(dataset):
            return []
        idx_range = index_range(page, page_size)
        start_idx = idx_range[0]
        end_idx = idx_range[1]
        data_list = []
        for row in range(start_idx, end_idx):
            data_list.append(row)
        return data_list

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """returns a dictionary with the data"""
        data_list = self.get_page(page, page_size)
        dataset = self.dataset()
        total_p = math.ceil(len(dataset) / page_size)
        next_p = page + 1
        if next_p > total_p:
            next_p = None
        prev_p = page - 1
        if prev_p < 0:
            prev_p = None

        data_dict = {'page_size': page_size,
                'page': page,
                'data': data_list,
                'next_page': next_p,
                'prev_page': prev_p,
                'total_pages': total_p
        }
        return data_dict
