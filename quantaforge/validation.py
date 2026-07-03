"""
quantaforge.validation
~~~~~~~~~~~~~~~~~~~~~~

Validation utilities for QuantaForge.
"""

from __future__ import annotations

from typing import Any

from .exceptions import ValidationError


class Validator:
    """
    Base validator.
    """

    def validate(self, value: Any) -> Any:
        return value


class TypeValidator(Validator):
    """
    Validate the expected type.
    """

    def __init__(self, expected_type: type | tuple[type, ...]) -> None:
        self.expected_type = expected_type

    def validate(self, value: Any) -> Any:
        if not isinstance(value, self.expected_type):
            raise ValidationError(
                f"Expected {self.expected_type}, got {type(value).__name__}."
            )
        return value


class RangeValidator(Validator):
    """
    Validate numeric ranges.
    """

    def __init__(
        self,
        minimum: float | None = None,
        maximum: float | None = None,
    ) -> None:
        self.minimum = minimum
        self.maximum = maximum

    def validate(self, value: float) -> float:
        if self.minimum is not None and value < self.minimum:
            raise ValidationError(
                f"Value must be greater than or equal to {self.minimum}."
            )

        if self.maximum is not None and value > self.maximum:
            raise ValidationError(
                f"Value must be less than or equal to {self.maximum}."
            )

        return value


class LengthValidator(Validator):
    """
    Validate object length.
    """

    def __init__(
        self,
        minimum: int | None = None,
        maximum: int | None = None,
    ) -> None:
        self.minimum = minimum
        self.maximum = maximum

    def validate(self, value: Any) -> Any:
        length = len(value)

        if self.minimum is not None and length < self.minimum:
            raise ValidationError(
                f"Length must be at least {self.minimum}."
            )

        if self.maximum is not None and length > self.maximum:
            raise ValidationError(
                f"Length must not exceed {self.maximum}."
            )

        return value


class CompositeValidator(Validator):
    """
    Combine multiple validators.
    """

    def __init__(self, *validators: Validator) -> None:
        self.validators = validators

    def validate(self, value: Any) -> Any:
        for validator in self.validators:
            value = validator.validate(value)

        return value
