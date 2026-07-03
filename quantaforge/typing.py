"""
quantaforge.typing
~~~~~~~~~~~~~~~~~~

Shared type definitions used across QuantaForge.
"""

from __future__ import annotations

from collections.abc import Awaitable, Callable, Mapping
from typing import Any, Protocol, TypeAlias, TypeVar

T = TypeVar("T")
R = TypeVar("R")

JSONPrimitive: TypeAlias = str | int | float | bool | None
JSONValue: TypeAlias = (
    JSONPrimitive
    | list["JSONValue"]
    | dict[str, "JSONValue"]
)

TaskResult: TypeAlias = Any
TaskArguments: TypeAlias = tuple[Any, ...]
TaskKeywordArguments: TypeAlias = dict[str, Any]

SyncTask: TypeAlias = Callable[..., TaskResult]
AsyncTask: TypeAlias = Callable[..., Awaitable[TaskResult]]

TaskCallable: TypeAlias = SyncTask | AsyncTask

Metadata: TypeAlias = dict[str, Any]

Config: TypeAlias = Mapping[str, Any]


class SupportsRun(Protocol):
    """
    Represents any object exposing a run() method.
    """

    def run(self) -> Any:
        ...


class SupportsAsyncRun(Protocol):
    """
    Represents any object exposing an async run() method.
    """

    async def run(self) -> Any:
        ...


class SupportsValidate(Protocol):
    """
    Represents a validator implementation.
    """

    def validate(self, value: Any) -> bool:
        ...


class SupportsSerialize(Protocol):
    """
    Represents an object that can be serialized.
    """

    def to_dict(self) -> dict[str, Any]:
        ...


__all__ = [
    "T",
    "R",
    "JSONPrimitive",
    "JSONValue",
    "TaskResult",
    "TaskArguments",
    "TaskKeywordArguments",
    "TaskCallable",
    "SyncTask",
    "AsyncTask",
    "Metadata",
    "Config",
    "SupportsRun",
    "SupportsAsyncRun",
    "SupportsValidate",
    "SupportsSerialize",
]
