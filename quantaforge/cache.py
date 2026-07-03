"""
quantaforge.cache
~~~~~~~~~~~~~~~~~

Lightweight in-memory cache implementation.
"""

from __future__ import annotations

import threading
import time
from typing import Any


class CacheItem:
    """
    Represents a cached value.
    """

    __slots__ = ("value", "expires_at")

    def __init__(self, value: Any, ttl: float | None = None) -> None:
        self.value = value
        self.expires_at = (
            None if ttl is None else time.time() + ttl
        )

    @property
    def expired(self) -> bool:
        if self.expires_at is None:
            return False
        return time.time() >= self.expires_at


class MemoryCache:
    """
    Thread-safe in-memory cache.
    """

    def __init__(self) -> None:
        self._storage: dict[str, CacheItem] = {}
        self._lock = threading.RLock()

    def set(
        self,
        key: str,
        value: Any,
        ttl: float | None = None,
    ) -> None:
        with self._lock:
            self._storage[key] = CacheItem(value, ttl)

    def get(
        self,
        key: str,
        default: Any = None,
    ) -> Any:
        with self._lock:

            item = self._storage.get(key)

            if item is None:
                return default

            if item.expired:
                del self._storage[key]
                return default

            return item.value

    def exists(self, key: str) -> bool:
        return self.get(key) is not None

    def delete(self, key: str) -> bool:
        with self._lock:
            return self._storage.pop(key, None) is not None

    def clear(self) -> None:
        with self._lock:
            self._storage.clear()

    def cleanup(self) -> int:
        """
        Remove expired entries.
        """

        removed = 0

        with self._lock:

            for key in list(self._storage):

                if self._storage[key].expired:
                    del self._storage[key]
                    removed += 1

        return removed

    def size(self) -> int:
        self.cleanup()
        return len(self._storage)

    def keys(self) -> list[str]:
        self.cleanup()
        return list(self._storage.keys())

    def values(self) -> list[Any]:
        self.cleanup()
        return [item.value for item in self._storage.values()]

    def items(self) -> dict[str, Any]:
        self.cleanup()

        return {
            key: item.value
            for key, item in self._storage.items()
        }

    def __contains__(self, key: str) -> bool:
        return self.exists(key)

    def __len__(self) -> int:
        return self.size()

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"(size={self.size()})"
  )
