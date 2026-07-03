"""
quantaforge.utils
~~~~~~~~~~~~~~~~~

Shared utility helpers for QuantaForge.
"""

from __future__ import annotations

import hashlib
import logging
import secrets
import string
import time
import uuid
from collections.abc import Callable
from functools import wraps
from typing import Any, TypeVar

T = TypeVar("T")

_LOGGER = logging.getLogger("quantaforge")


def configure_logging(level: int = logging.INFO) -> None:
    """
    Configure the default QuantaForge logger.
    """
    if _LOGGER.handlers:
        return

    handler = logging.StreamHandler()

    formatter = logging.Formatter(
        "[%(levelname)s] %(asctime)s | %(name)s | %(message)s"
    )

    handler.setFormatter(formatter)

    _LOGGER.addHandler(handler)
    _LOGGER.setLevel(level)


def get_logger() -> logging.Logger:
    """
    Return the framework logger.
    """
    return _LOGGER


def generate_uuid() -> str:
    """
    Generate a UUID4 string.
    """
    return str(uuid.uuid4())


def generate_token(length: int = 32) -> str:
    """
    Generate a secure random token.
    """
    alphabet = string.ascii_letters + string.digits
    return "".join(secrets.choice(alphabet) for _ in range(length))


def sha256(value: str) -> str:
    """
    Return the SHA-256 hash of a string.
    """
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def current_timestamp() -> float:
    """
    Return the current UNIX timestamp.
    """
    return time.time()


def execution_timer(func: Callable[..., T]) -> Callable[..., T]:
    """
    Measure execution time of a function.
    """

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> T:
        start = time.perf_counter()

        result = func(*args, **kwargs)

        elapsed = time.perf_counter() - start

        _LOGGER.info(
            "%s executed in %.6f seconds",
            func.__name__,
            elapsed,
        )

        return result

    return wrapper


def retry(
    attempts: int = 3,
    delay: float = 0.5,
) -> Callable[[Callable[..., T]], Callable[..., T]]:
    """
    Retry a function if it raises an exception.
    """

    def decorator(func: Callable[..., T]) -> Callable[..., T]:

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> T:

            last_error: Exception | None = None

            for _ in range(attempts):
                try:
                    return func(*args, **kwargs)

                except Exception as exc:
                    last_error = exc
                    time.sleep(delay)

            assert last_error is not None

            raise last_error

        return wrapper

    return decorator


def deep_merge(
    left: dict[str, Any],
    right: dict[str, Any],
) -> dict[str, Any]:
    """
    Deep merge two dictionaries.
    """

    merged = left.copy()

    for key, value in right.items():

        if (
            key in merged
            and isinstance(merged[key], dict)
            and isinstance(value, dict)
        ):
            merged[key] = deep_merge(merged[key], value)

        else:
            merged[key] = value

    return merged
