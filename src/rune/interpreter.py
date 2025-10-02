"""
INTERPRETER:
This is the base Rune interpreter
"""""
from lark import Transformer
from textual.widgets import Button, Input, Static, Header, Footer
from textual.containers import Grid, Horizontal, Vertical
from dataclasses import dataclass

# Note: textual.layout.Layout is not a widget, but a container.
# textual.containers.Container might be what you mean, or you can
# just use the specific containers like Grid, Horizontal, Vertical.
WIDGET_MAP = {
    "input": Input,
    "button": Button,
    "horizontal": Horizontal,
    "vertical": Vertical,
    "grid": Grid,
    "static": Static, # It's good to have a generic static widget
    "header": Header,
    "footer": Footer
}

@dataclass
class CSSId:
    name: str

@dataclass
class CSSClass:
    name: str
class RuneTransformer(Transformer):
    def ID(self, token):
        return str(token)
    
    def ESCAPED_STRING(self, token):
        return token[1:-1]
    
    def SIGNED_NUMBER(self, token):
        return int(token)
    def start(self, items):
        return items
    
    def true(self, items):
        return True
    
    def false(self, items):
        return False

    def id(self, items): # Using id() is fine, but id_() is safer to not shadow the built-in
        return CSSId(name=str(items[0]))

    def class_(self, items):
        return CSSClass(name=str(items[0]))
    
    def block(self, items):
        return items

    def statement(self, items: list):
        # Pass the processed child (component or content) up the tree
        return items[0]

    def content(self, items: list):
        # Turn a raw string into a Static widget
        return Static(items[0])

    def value(self, items):
        return items[0]

    def key_value(self, items: list) -> tuple:
        print(f"DEBUG [key_value] received: {items!r}")
        return (items[0], items[1])
    
    def parameters(self, items: list) -> dict:
        return dict(items)
       
    
    def component(self, items):
        # Set default values
        component_name = items.pop(0) # The first item is always the name
        css_id = None
        css_class = None
        parameters = {}
        block_content = None

        # Flexibly find the parts by their type
        for item in items:
            if isinstance(item, CSSId):
                css_id = item.name
            elif isinstance(item, CSSClass):
                css_class = item.name
            elif isinstance(item, dict):
                parameters = item
            elif isinstance(item, list):
                block_content = item

        # The rest of your logic stays the same!
        widget_class = WIDGET_MAP.get(str(component_name))
        if not widget_class:
            raise NameError(f"Unknown component '{component_name}'")

        widget = widget_class()
        
        kwargs = {}
        if css_id:
            widget.id = css_id
        if css_class:
            widget.classes = css_class
        if parameters:
            for key, value in parameters.items():
                setattr(widget, key, value)

        widget = widget_class(**kwargs)

        if block_content:
            if hasattr(widget, 'mount'):
                widget.mount(*block_content)
            else:
                raise TypeError(f"Component '{component_name}' cannot contain nested children.")

        return widget