#!/usr/bin/env python3
"""LRU Caching
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """A caching class that implements Least Recently Used caching policy
    """
    order = {}
    evict_order = []    # First item is LRU

    def put(self, key, item):
        """Insert an item in the cache
        """
        if key is None or item is None:
            return

        if (len(self.cache_data) == BaseCaching.MAX_ITEMS and
                key not in self.cache_data):
            discarded = self.evict()
            print("DISCARD: {}".format(discarded[0]))

        self.cache_data[key] = item
        self.evict_ping(key)

    def evict(self):
        """Remove the least recently used key and item
        """
        if len(self.evict_order) <= 0:
            return None, None

        key = self.evict_order[0]
        val = self.cache_data[key]

        # Delete from cache
        self.cache_data.pop(key)

        # Update evict order
        self.evict_order.remove(key)

        return key, val

    def evict_ping(self, key):
        """Update evict order
        """
        if key in self.evict_order:
            self.evict_order.remove(key)

        self.evict_order.append(key)

    def pop(self):
        """Remove the least recently used key and item
        """
        min_used = None
        equal_use = True

        # Find the least used item
        for key, val in self.order.items():
            if not min_used:
                min_used = key
                continue

            if val != self.order[min_used]:
                equal_use = False
            if val < self.order[min_used]:
                min_used = key

        # If all items are equally used, use FIFO to evict cache block
        # I.e evict the first item to enter the cache
        # NB: Dictionaries maintain items in order of insertion
        # So, I can easily evict the very first item while iterating
        # through the dictionary
        if equal_use:
            for key, val in self.order.items():
                min_used = key
                break

        # Removed item from cache
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

        self.evict_ping(key)
        return self.cache_data[key]
