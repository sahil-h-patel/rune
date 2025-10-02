from typing import List
from textual.widget import Widget
from .parser import parser
from .interpreter import RuneTransformer

def load(filepath: str):
    with open(filepath, "r") as f:
        source_code = f.read()
    ast = parser.parse(source_code)
    app = RuneTransformer().transform(ast)
    if not isinstance(app, list):
        app = [app]
    return app