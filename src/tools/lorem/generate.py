from os import getenv
from random import choices
from core.filemanip import load, Format
from core.path import Path

WORDS: set[str] = load(f'{Path.SRC}\\tools\\lorem\\words.json', Format.JSON)
def generate(length: int) -> str:
    match length:
        case 1: return 'Lorem'
        case 2: return 'Lorem ipsum'
        case _:
            text: str = ' '.join(choices(WORDS, k=length - 2))
            return f'Lorem ipsum {text}'

def main() -> str:
    length: int = int(getenv(key='ESPANSO_LEN'))
    return generate(length)