from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget


class TuringGrid(Widget):
    def change_alphabet(self):
        # TODO
        # Implement a window allowing to change the alphabet
        pass

    def change_state_list(self):
        # TODO
        # Implement a window allowing to change the state_list
        pass

    def change_state_diagram(self):
        # TODO
        # Implement a window allowing to change the state_diagram
        pass

class TuringGUI(App):
    def build(self):
        return TuringGrid()


TuringGUI().run()
