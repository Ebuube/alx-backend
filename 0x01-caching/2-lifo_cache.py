#!/usr/bin/env python3
"""LIFO caching
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """A caching class that implements LIFO caching policy
    """
    order = {}

    def put(self, key, item):
        """Insert an item into cache using LIFO caching policy
        """
        if key is None or item is None:
            return

        if (len(self.cache_data) == BaseCaching.MAX_ITEMS and
                key not in self.cache_data):
            discarded = self.pop()
            print("DISCARD: {}".format(discarded[0]))

        # Insert item
        self.cache_data[key] = item
        if self.order:
            index = max(self.order) + 1
            self.order[index] = key
        else:
            index = 0
            self.order[index] = key

    def pop(self):
        """Remove the last item inserted
        """
        if not self.order:
            return None

        index = max(self.order)
        key = self.order[index]
        item = self.cache_data.pop(key)

        self.order.pop(max(self.order))     # Shorten order
        return key, item

    def get(self, key):
        """Fetch an item from cache
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
