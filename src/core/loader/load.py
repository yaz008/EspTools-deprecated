from importlib import import_module
from core.filemanip import load, Format
from core.path import Config
from typing import Any, Callable
from types import ModuleType

def loadattr(module: str, name: str) -> Any:
    module: ModuleType = import_module(name=module)
    return getattr(module, name)

TOOLS: dict[str, str] = load(Config.TOOLS, Format.JSON)
def load_tool(name: str) -> Callable[[], str]:
    tool: str = TOOLS[name]
    return loadattr(module=f'tools.{tool}', name='main')