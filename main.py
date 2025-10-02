from textual.app import App, ComposeResult
import rune

BINDINGS = [
    ("ctrl+c", "quit", "Quit"),
]
class MyApp(App):
    def compose(self) -> ComposeResult:
        yield from rune.load("login_form.rune")

MyApp().run()