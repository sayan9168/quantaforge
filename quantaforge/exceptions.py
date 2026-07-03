"""
quantaforge.exceptions
~~~~~~~~~~~~~~~~~~~~~~

Custom exception hierarchy for QuantaForge.
"""

from __future__ import annotations


class QuantaForgeError(Exception):
    """
    Base exception for all QuantaForge errors.
    """

    default_message = "An unknown QuantaForge error occurred."

    def __init__(self, message: str | None = None) -> None:
        self.message = message or self.default_message
        super().__init__(self.message)


class PipelineError(QuantaForgeError):
    """
    Raised when a pipeline fails.
    """

    default_message = "Pipeline execution failed."


class TaskError(PipelineError):
    """
    Raised when a task fails.
    """

    default_message = "Task execution failed."


class ValidationError(QuantaForgeError):
    """
    Raised when validation fails.
    """

    default_message = "Validation failed."


class CacheError(QuantaForgeError):
    """
    Raised when cache operations fail.
    """

    default_message = "Cache operation failed."


class PluginError(QuantaForgeError):
    """
    Raised for plugin-related errors.
    """

    default_message = "Plugin error."


class DependencyError(QuantaForgeError):
    """
    Raised when dependency injection fails.
    """

    default_message = "Dependency resolution failed."


class SchedulerError(QuantaForgeError):
    """
    Raised when scheduler execution fails.
    """

    default_message = "Scheduler error."


class ConfigurationError(QuantaForgeError):
    """
    Raised when configuration is invalid.
    """

    default_message = "Invalid configuration."


class SerializationError(QuantaForgeError):
    """
    Raised when serialization or deserialization fails.
    """

    default_message = "Serialization error."


class EventError(QuantaForgeError):
    """
    Raised for event system failures.
    """

    default_message = "Event dispatch failed."
