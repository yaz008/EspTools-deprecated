from os import getenv
from random import choices
from re import findall
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
    expr: str = getenv(key='ESPANSO_EXPR')
    if expr == '':
        return generate(length=10)

    result: str = ''

    pattern: str = r'(?:[\\./]|[0-9]+)'
    for token in findall(pattern=pattern, string=expr):
        match token:
            case '.': result += '. '
            case '/': result += '\n'
            case number:
                result += generate(length=int(number))

    return result