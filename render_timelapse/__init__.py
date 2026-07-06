"""
Register & unregister add-on modules, i.e. entry/exit point.
"""

import tomllib
from pathlib import Path

from . import panel, rendering, tracking
from .log import get_logger

# Logging object instead of print
_logger = get_logger()

# Load version for logging
_manifest = tomllib.loads(Path(__file__).with_name("blender_manifest.toml").read_text())
_version = _manifest["version"]

# Modules that the add-on registers
_modules = (panel, tracking, rendering)


def register():
    for module in _modules:
        module.register()
    _logger.debug(f"v{_version} registered")


def unregister():
    for module in reversed(_modules):
        module.unregister()
    _logger.debug("unregistered\n")
