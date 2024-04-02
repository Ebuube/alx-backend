#!/usr/bin/env python3
"""MRU Caching
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """A caching class that implements Most Recently Used caching policy
    """
    order = []  # Last item is MRU

    def put(self, key, item):
        """Insert an item in the cache
        """
        if key is None or item is None:
            return

        if (len(self.cache_data) >= BaseCaching.MAX_ITEMS and
                key not in self.cache_data):
            discarded = self.evict()
            print("DISCARD: {}".format(discarded[0]))

        self.cache_data[key] = item
        self.ping(key)

    def evict(self):
        """Remove the most recently used key and item
        """
        if len(self.order) <= 0:
            return None, None

        key = self.order[-1]
        val = self.cache_data[key]

        # Delete from cache
        self.cache_data.pop(key)

        # Update eviction order
        self.order.remove(key)

        return key, val

    def ping(self, key):
        """Update eviction order
        """
        if key in self.order:
            self.order.remove(key)

        self.order.append(key)

    def get(self, key):
        """Fetch the specified data from the cache
        """
        if key is None or key not in self.cache_data:
            return None

        self.ping(key)
        return self.cache_data[key]
