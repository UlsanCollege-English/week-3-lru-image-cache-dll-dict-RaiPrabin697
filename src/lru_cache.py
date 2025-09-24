# src/lru_cache.py
from collections import OrderedDict
from typing import Any, Optional

class LRUCache:
    def __init__(self, capacity: int):
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("capacity must be a positive integer")
        self.capacity = capacity
        self._data = OrderedDict()

    def get(self, key: Any) -> Optional[Any]:
        """Return value for key or None if missing. Marks key as most-recent."""
        if key not in self._data:
            return None
        self._data.move_to_end(key)   # mark as most recently used
        return self._data[key]

    def put(self, key: Any, value: Any) -> None:
        """Insert or update key. Evict least-recent if capacity exceeded."""
        if key in self._data:
            # update value and mark most recent
            self._data[key] = value
            self._data.move_to_end(key)
            return
        # new key
        self._data[key] = value
        if len(self._data) > self.capacity:
            # pop least recently used (first item)
            self._data.popitem(last=False)

    def __contains__(self, key: Any) -> bool:
        return key in self._data

    def __repr__(self) -> str:
        # order from least-recent to most-recent
        keys = list(self._data.keys())
        return f"LRUCache(capacity={self.capacity}, order={keys})"