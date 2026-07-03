"""
quantaforge.pipeline
~~~~~~~~~~~~~~~~~~~~

Core pipeline implementation.
"""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

from .cache import MemoryCache
from .context import ExecutionContext
from .events import EventDispatcher
from .executor import TaskExecutor
from .validation import Validator


class Pipeline:
    """
    Core pipeline implementation.
    """

    def __init__(self) -> None:
        self._tasks: list[Callable[..., Any]] = []

        self.context = ExecutionContext()

        self.cache = MemoryCache()

        self.events = EventDispatcher()

        self.executor = TaskExecutor(
            context=self.context,
            dispatcher=self.events,
        )

    def task(
        self,
        func: Callable[..., Any],
    ) -> Callable[..., Any]:
        """
        Register a task.
        """

        self._tasks.append(func)

        return func

    def add_task(
        self,
        func: Callable[..., Any],
    ) -> None:
        """
        Register a task manually.
        """

        self._tasks.append(func)

    @property
    def tasks(self) -> tuple[Callable[..., Any], ...]:
        """
        Return registered tasks.
        """

        return tuple(self._tasks)

    def clear(self) -> None:
        """
        Remove all tasks.
        """

        self._tasks.clear()

    def validate(
        self,
        validator: Validator,
        value: Any,
    ) -> Any:
        """
        Validate a value.
        """

        return validator.validate(value)
