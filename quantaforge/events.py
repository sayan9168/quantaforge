"""
quantaforge.events
~~~~~~~~~~~~~~~~~~

Simple event dispatcher for QuantaForge.
"""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Callable
from typing import Any

EventHandler = Callable[..., Any]


class EventDispatcher:
    """
    Lightweight synchronous event dispatcher.
    """

    def __init__(self) -> None:
        self._listeners: dict[str, list[EventHandler]] = defaultdict(list)

    def on(
        self,
        event: str,
        handler: EventHandler,
    ) -> None:
        """
        Register an event handler.
        """
        if handler not in self._listeners[event]:
            self._listeners[event].append(handler)

    def off(
        self,
        event: str,
        handler: EventHandler,
    ) -> bool:
        """
        Remove an event handler.
        """
        listeners = self._listeners.get(event)

        if not listeners:
            return False

        try:
            listeners.remove(handler)
            return True
        except ValueError:
            return False

    def emit(
        self,
        event: str,
        *args: Any,
        **kwargs: Any,
    ) -> list[Any]:
        """
        Emit an event and collect handler results.
        """
        results: list[Any] = []

        for handler in self._listeners.get(event, []):
            results.append(handler(*args, **kwargs))

        return results

    def clear(self, event: str | None = None) -> None:
        """
        Remove handlers.
        """
        if event is None:
            self._listeners.clear()
        else:
            self._listeners.pop(event, None)

    def listeners(self, event: str) -> tuple[EventHandler, ...]:
        """
        Return registered handlers.
        """
        return tuple(self._listeners.get(event, ()))

    def has_listeners(self, event: str) -> bool:
        """
        Check whether an event has listeners.
        """
        return bool(self._listeners.get(event))

    @property
    def registered_events(self) -> tuple[str, ...]:
        """
        Return all registered event names.
        """
        return tuple(self._listeners.keys())

    def __len__(self) -> int:
        return sum(len(v) for v in self._listeners.values())

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"(events={len(self._listeners)}, "
            f"listeners={len(self)})"
    )
