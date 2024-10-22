from os import environ
from sys import path
from enum import StrEnum

class Path(StrEnum):
    SRC: str = path[0]
    ESPANSO: str = environ['CONFIG']

class Config(StrEnum):
    TOOLS: str = f'{path[0]}\\tools\\config.json'