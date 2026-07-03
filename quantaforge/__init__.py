"""
QuantaForge
============

A next-generation Python framework for intelligent pipelines,
asynchronous execution, caching, validation, and plugin architecture.
"""

from __future__ import annotations

__title__ = "quantaforge"
__version__ = "0.1.0"
__author__ = "Sayan"
__license__ = "Sayanox License 1.1"

from .context import ExecutionContext
from .exceptions import (
    QuantaForgeError,
    PipelineError,
    ValidationError,
    CacheError,
    PluginError,
)
from .pipeline import Pipeline

__all__ = [
    "Pipeline",
    "ExecutionContext",
    "QuantaForgeError",
    "PipelineError",
    "ValidationError",
    "CacheError",
    "PluginError",
]
