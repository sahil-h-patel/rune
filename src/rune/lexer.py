"""
LEXER:
This is where the tokenization happens
"""
from lark import Lark

current_dir = Path(__file__).parent
grammar_filepath = current_dir / "rune.lark"

parser = Lark.open(grammar_filepath, parser="lalr")





