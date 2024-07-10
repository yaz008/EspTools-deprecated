from os import getenv
from random import choices
from re import findall
from random import randint
from core.filemanip import load, Format
from core.path import Path

WORDS: set[str] = load(f'{Path.SRC}\\tools\\lorem\\words.json', Format.JSON)
def generate_sentence(length: int) -> str:
    match length:
        case 1: return 'Lorem'
        case 2: return 'Lorem ipsum'
        case _:
            text: str = ' '.join(choices(WORDS, k=length - 2))
            return f'Lorem ipsum {text}'
        
def generate(expr: str) -> str:
    result: str = ''
    for token in findall(pattern=r'(?:[\\./]|[0-9]+)', string=expr):
        match token:
            case '.': result += '. '
            case '/': result += '\n'
            case number:
                result += generate_sentence(length=int(number))
    return result
        
def generate_sentences_expr(number: int) -> str:
    return '.'.join([str(randint(5, 15)) for _ in range(number)])

def generate_paragraphs_expr(number: str) -> str:
    return '/'.join([generate_sentences_expr(randint(3, 5)) for _ in range(number)])

def main() -> str:
    expr: str = getenv(key='ESPANSO_EXPR')
    if expr == '':
        expr = '10'
    if expr[-1] == 's':
        expr = generate_sentences_expr(number=int(expr[:-1]))
    if expr[-1] == 'p':
        expr = generate_paragraphs_expr(number=int(expr[:-1]))
    return generate(expr=expr)