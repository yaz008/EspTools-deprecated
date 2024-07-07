from importlib import import_module
from typing import Any
from types import ModuleType

def loadattr(module: str, name: str) -> Any:
    module: ModuleType = import_module(name=module)
    return getattr(module, name)