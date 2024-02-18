#!/usr/bin/env python3
"""Hypermedia Pagination"""
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
        assert type(page) is int
        assert type(page_size) is int
        assert (page > 0) and (page_size > 0)
        data_range = index_range(page, page_size)
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
            count += 1

        return data

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Get a page as hypermedia

        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no pervious page
        total_pages: the total number of pages in the dataset as an integer
        """
        data = self.get_page(page, page_size)
        data_size = len(data)

        hyper = {}
        hyper['page_size'] = data_size
        hyper['page'] = page
        hyper['data'] = data

        # Set next page
        try:
            if self.__dataset[index_range(page + 1, page_size)[0]]:
                hyper['next_page'] = page + 1
        except IndexError:
            hyper['next_page'] = None

        # Set previous page
        try:
            if page < 2:
                raise IndexError('First page does not have a previous page')

            if self.__dataset[index_range(page - 1, page_size)[0]]:
                hyper['prev_page'] = page - 1
        except IndexError:
            hyper['prev_page'] = None

        # Set total pages
        if self.__dataset:
            total_size = len(self.__dataset)
            hyper['total_pages'] = math.ceil(total_size / page_size)

        return hyper
