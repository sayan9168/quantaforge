"""
quantaforge.context
~~~~~~~~~~~~~~~~~~~

Execution context for QuantaForge.
"""

from __future__ import annotations

from typing import Any


class ExecutionContext:
    """
    Shared execution context used across the framework.
    """

    def __init__(self) -> None:
        self._state: dict[str, Any] = {}
        self._metadata: dict[str, Any] = {}

    def set(self, key: str, value: Any) -> None:
        """
        Store a value.
        """
        self._state[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        """
        Retrieve a value.
        """
        return self._state.get(key, default)

    def remove(self, key: str) -> bool:
        """
        Remove a value.
        """
        return self._state.pop(key, None) is not None

    def exists(self, key: str) -> bool:
        """
        Check whether a key exists.
        """
        return key in self._state

    def clear(self) -> None:
        """
        Remove all stored values.
        """
        self._state.clear()

    def update(self, values: dict[str, Any]) -> None:
        """
        Update multiple values.
        """
        self._state.update(values)

    def metadata(self, key: str, value: Any) -> None:
        """
        Store metadata.
        """
        self._metadata[key] = value

    def get_metadata(
        self,
        key: str,
        default: Any = None,
    ) -> Any:
        """
        Retrieve metadata.
        """
        return self._metadata.get(key, default)

    @property
    def state(self) -> dict[str, Any]:
        """
        Return a copy of the current state.
        """
        return self._state.copy()

    @property
    def meta(self) -> dict[str, Any]:
        """
        Return a copy of the metadata.
        """
        return self._metadata.copy()

    def __contains__(self, key: str) -> bool:
        return self.exists(key)

    def __len__(self) -> int:
        return len(self._state)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"(items={len(self._state)})"
        )
