#!/usr/bin/env python3
"""LRU Caching
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """A caching class that implements Least Recently Used caching policy
    """
    order = {}

    def put(self, key, item):
        """Insert an item in the cache

        Concept: Dictionaries maintain their order of insertion
        """
        if key is None or item is None:
            return
            
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Access the oldest inserted item
            lru_key = next(iter(self.cache_data))
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}\n")
            
        self.cache_data[key] = item

    def pop(self):
        """Remove the least recently used key and item
        """
        min_used = None
        equal_use = True
        for key, val in self.order.items():
            if not min_used:
                min_used = key
                continue

            if val != self.order[min_used]:
                equal_use = False
            if val < self.order[min_used]:
                min_used = key

        # If equally used, use FIFO to evict cache block
        if equal_use:
            for key, val in self.order.items():
                min_used = key
                break

        item = self.cache_data.pop(min_used)

        # update order
        self.order.pop(min_used)
        for key in self.order:
            self.order[key] = self.order[key] - 1

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

        return self.cache_data[key]
