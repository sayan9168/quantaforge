"""
quantaforge.dependency
~~~~~~~~~~~~~~~~~~~~~~

Dependency injection container.
"""

from __future__ import annotations

from typing import Any


class DependencyContainer:
    """
    Lightweight dependency injection container.
    """

    def __init__(self) -> None:
        self._services: dict[str, Any] = {}

    def register(
        self,
        name: str,
        service: Any,
    ) -> None:
        """
        Register a service.
        """
        self._services[name] = service

    def resolve(self, name: str) -> Any:
        """
        Resolve a registered service.
        """
        try:
            return self._services[name]
        except KeyError as exc:
            raise KeyError(
                f"Service '{name}' is not registered."
            ) from exc

    def unregister(self, name: str) -> bool:
        """
        Remove a registered service.
        """
        return self._services.pop(name, None) is not None

    def exists(self, name: str) -> bool:
        """
        Check whether a service exists.
        """
        return name in self._services

    def clear(self) -> None:
        """
        Remove all registered services.
        """
        self._services.clear()

    def services(self) -> tuple[str, ...]:
        """
        Return all registered service names.
        """
        return tuple(self._services.keys())

    def __contains__(self, name: str) -> bool:
        return self.exists(name)

    def __len__(self) -> int:
        return len(self._services)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"(services={len(self)})"
        )
