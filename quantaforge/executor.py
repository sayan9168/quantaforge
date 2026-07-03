"""
quantaforge.executor
~~~~~~~~~~~~~~~~~~~~

Task execution engine.
"""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

from .context import ExecutionContext
from .events import EventDispatcher


class TaskExecutor:
    """
    Executes registered tasks.
    """

    def __init__(
        self,
        context: ExecutionContext,
        dispatcher: EventDispatcher,
    ) -> None:
        self._context = context
        self._dispatcher = dispatcher

    def execute(
        self,
        task: Callable[..., Any],
        *args: Any,
        **kwargs: Any,
    ) -> Any:
        """
        Execute a single task.
        """

        task_name = task.__name__

        self._dispatcher.emit(
            "task.before_execute",
            task_name,
        )

        result = task(*args, **kwargs)

        self._context.set(task_name, result)

        self._dispatcher.emit(
            "task.after_execute",
            task_name,
            result,
        )

        return result
