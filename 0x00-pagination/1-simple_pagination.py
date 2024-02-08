#!/usr/bin/env python3
"""Simple Pagination"""
import csv
import math
from typing import List


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
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initialize instance of server
        """
        self.__dataset = None

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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a page
        """
        assert(page > 0 and page_size > 0)
        data_range = index_range(page, page_size)
        print("data range: {} <-> {}".format(data_range[0], data_range[1])) # test
        data = []
        dataset = self.dataset()
        count = 0

        for row in dataset:
            if count < data_range[0]:
                count += 1
                continue
            if count >= data_range[1]:
                break

            data.append(row)
            print("count: {}\t|\t{}".format(count, row))    # test
            count += 1

        return data
