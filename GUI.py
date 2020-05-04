from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.core.window import Window

#Window.fullscreen = 'auto'


class TuringLayout(FloatLayout):
    def change_alphabet(self):
        # TODO
        # Implement UI inside the popup allowing change the alphabet
        class AlphabetPopup(FloatLayout):
            pass
        window = AlphabetPopup()
        popup = Popup(title="Modyfikowanie alfabetu", content=window, size_hint=(None, None), size=(400, 400))
        popup.open()

    def change_state_list(self):
        # TODO
        # Implement a window allowing to change the state_list
        class StatePopup(FloatLayout):
            pass

        window = StatePopup()
        popup = Popup(title="Modyfikowanie stanow", content=window, size_hint=(None, None), size=(400, 400))
        popup.open()

    def change_state_diagram(self):
        # TODO
        # Implement a window allowing to change the state_diagram
        class DiagramPopup(FloatLayout):
            pass

        window = DiagramPopup()
        popup = Popup(title="Modyfikowanie diagramu", content=window, size_hint=(None, None), size=(400, 400))
        popup.open()


class TuringGUI(App):
    def build(self):
        return TuringLayout()


TuringGUI().run()
