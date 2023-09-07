#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """when certain rows are removed from the db,
            the user does not miss items from db when changing page.
        """
        indexed_data_list = self.indexed_dataset()
        data_list = self.dataset()
        assert index <= len(data_list)

        start_idx = index
        end_idx = index + page_size
        filtered_data_list = []
        for i in range(start_idx, end_idx):
            if i in indexed_data_list:
                selected_data_list.append(indexed_data_list[i])

        data_dict = {'index': index,
                     'data': filtered_data_list,
                     'page_size': page_size,
                     'next_index': end_idx}
        return data_dict

