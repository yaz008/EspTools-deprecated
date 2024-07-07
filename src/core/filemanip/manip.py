from importlib import import_module
from enum import Enum
from typing import Any
from types import ModuleType

BIN: bool = True

class Format(Enum):
    JSON: tuple[str, bool] = ('json', not BIN)
    PICKLE: tuple[str, bool] = ('pickle', BIN)
    
def unpack(fmt: Format, open_mode: str) -> tuple[str, str]:
    module, mode = fmt.value
    if mode is BIN:
        open_mode += 'b'
    return module, open_mode

def load(path: str, fmt: Format) -> Any:
    module, mode = unpack(fmt, open_mode='r')
    loader: ModuleType = import_module(name=module)
    with open(file=path, mode=mode) as File:
        return loader.load(File)
    
def dump(path: str, obj: Any, fmt: Format) -> None:
    module, mode = unpack(fmt, open_mode='w')
    dumper: ModuleType = import_module(name=module)
    with open(file=path, mode=mode) as File:
        dumper.dump(obj, File)