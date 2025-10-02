"""
PARSER:
This is the base Rune parser
"""
from lark import Lark
from pathlib import Path

current_dir = Path(__file__).parent
grammar_filepath = current_dir / "grammar.lark"
parser = Lark.open(grammar_filepath, parser="lalr")




