from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static
from textual.containers import Horizontal

class MyApp(App):
    BINDINGS = [
        ("ctrl+c", "quit", "Quit"),
    ]

    def compose(self) -> ComposeResult:
        yield Static("Hello World!")
        yield Horizontal(Static("Left"), Static("Center"), Static("Right"))

MyApp().run(inline=True)