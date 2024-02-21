#!/usr/bin/env python3
"""Basic dictionary
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A basic caching system with get and put implemented
    """
    def put(self, key, item):
        """Insert an item into cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Fetch in item from cache
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
