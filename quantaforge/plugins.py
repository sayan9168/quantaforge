"""
quantaforge.plugins
~~~~~~~~~~~~~~~~~~~

Plugin management system for QuantaForge.
"""

from __future__ import annotations

from typing import Any


class Plugin:
    """
    Base plugin class.
    """

    name: str = "plugin"
    version: str = "1.0.0"

    def enable(self) -> None:
        """
        Called when the plugin is enabled.
        """

    def disable(self) -> None:
        """
        Called when the plugin is disabled.
        """


class PluginManager:
    """
    Manages framework plugins.
    """

    def __init__(self) -> None:
        self._plugins: dict[str, Plugin] = {}

    def register(self, plugin: Plugin) -> None:
        """
        Register a plugin.
        """
        plugin.enable()
        self._plugins[plugin.name] = plugin

    def unregister(self, name: str) -> bool:
        """
        Remove a plugin.
        """
        plugin = self._plugins.pop(name, None)

        if plugin is None:
            return False

        plugin.disable()
        return True

    def get(self, name: str) -> Plugin | None:
        """
        Return a plugin.
        """
        return self._plugins.get(name)

    def all(self) -> tuple[Plugin, ...]:
        """
        Return all registered plugins.
        """
        return tuple(self._plugins.values())

    def exists(self, name: str) -> bool:
        """
        Check whether a plugin exists.
        """
        return name in self._plugins

    def clear(self) -> None:
        """
        Disable and remove all plugins.
        """
        for plugin in self._plugins.values():
            plugin.disable()

        self._plugins.clear()

    def __contains__(self, name: str) -> bool:
        return self.exists(name)

    def __len__(self) -> int:
        return len(self._plugins)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"(plugins={len(self)})"
        )
