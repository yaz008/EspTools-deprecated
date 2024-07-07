from sys import argv
from core.loader import load_tool
from typing import Callable

toolname: str = argv[1]
tool: Callable[[], str] = load_tool(toolname)
result: str = tool()
print(result)