#!/usr/bin/env python3
"""LFU Caching
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """A caching class that implements Least Frequency Used caching policy
    """
    order = {}

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
        """Remove the Least Frequency used key and item
        """
        min_used = None

        # Find the least ued item
        for key, val in self.order.items():
            if not min_used:
                min_used = key
                continue

            if val < self.order[min_used]:
                min_used = key

        # Evict first inserted item which is the least used
        # NB: Dictionaries maintain items in order of insertion
        # So, I can easily evict the very first item while iterating
        # through the dictionary
        for key, val in self.order.items():
            if val == self.cache_data[min_used]:
                min_used = key
                break

        # Remove the item from cache
        item = self.cache_data.pop(min_used)

        # Update eviction order
        self.order.pop(min_used)

        return min_used, item

    def ping(self, key):
        """Update use-count for a key
        """
        if key not in self.order:
            self.order[key] = 1
            return

        self.order[key] = self.order[key] + 1

    def get(self, key):
        """Fetch the specified data from the cache
        """
        if key is None or key not in self.cache_data:
            return None

        self.ping(key)
        return self.cache_data[key]
