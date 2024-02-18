#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""
import csv
import math
from typing import List, Dict


def index_range(page: int, page_size: int) -> tuple:
    """
    Return start and end index
    Page number starts from 1
    but range index starts from 0
    """
    start = page_size * (page - 1)
    end = page_size * page
    return (start, end)


class Server:
    """
    Server class to paginate a database of popular baby names
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initialize the instance
        """
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Dataset indexed by sorting position, startint at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                    i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Return an indexed page of items

        index: The index of the first item in the current page
        next_index: The index of the first item in the next page
        page_size: the current page size
        data: the actual page of the dataset
        """
        data_range = index_range(index, page_size)
        assert index in self.indexed_dataset()

        hyper_index = {}
        data = []
        hyper_index['index'] = index
        try:
            for x in range(page_size):
                data.append(self.indexed_dataset()[index])
                index += 1
                next_index = index
        except KeyError:
            pass

        try:
            if self.indexed_dataset()[next_index]:
                hyper_index['next_index'] = next_index
        except KeyError:
            hyper_index['next_index'] = None

        hyper_index['page_size'] = len(data)
        hyper_index['data'] = data

        return hyper_index
