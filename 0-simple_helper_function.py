#!/usr/bin/env python3
"""Simple helper function"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Return start and end index
    Page number starts from 1
    but range index starts from 0
    """
    start = page_size * (page - 1)
    end = page_size * page
    return (start, end)
