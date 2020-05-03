from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class TuringGrid(Widget):
    pass


class TuringGUI(App):
    def __init__(self):
        super().__init__()

    def build(self):
        return TuringGrid()


TuringGUI().run()
