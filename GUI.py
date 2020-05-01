from kivy.app import App
from kivy.uix.button import Button


class TuringGUI(App):
    def __init__(self):
        super().__init__()

    def build(self):
        return Button(text="Hello")


TuringGUI().run()
