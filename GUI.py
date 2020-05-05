from Turing import TuringMachine

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.spinner import Spinner
from kivy.core.window import Window
from kivy.properties import ObjectProperty, ListProperty, StringProperty

# Window.fullscreen = 'auto'

turing = TuringMachine()


class AlphabetList(Spinner):
    start = StringProperty(turing.alphabet[0] if len(turing.alphabet)>0 else "Brak wartosci")
    val = ListProperty(turing.alphabet)


    def update(self):
        self.start = StringProperty(turing.alphabet[0] if len(turing.alphabet) > 0 else "Brak wartosci")
        self.val = ListProperty(turing.alphabet)

class TuringLayout(FloatLayout):
    def change_alphabet(self):
        # TODO
        # Implement UI inside the popup allowing change the alphabet
        class AlphabetPopup(FloatLayout):
            new_chr = ObjectProperty(None)
            removed_chr = ObjectProperty(None)
            chr_list = turing.alphabet

            def add_chr(self):
                turing.alphabet_add(self.new_chr.text)
                AlphabetList.update()

            def del_chr(self):
                turing.alphabet_remove(self.removed_chr)
                AlphabetList.update()

        popup = Popup(title="Modify Alphabet", title_align="center", content=AlphabetPopup(), size_hint=(None, None), size=(400, 400))
        popup.open()


    def change_state_list(self):
        # TODO
        # Implement a window allowing to change the state_list
        class StatePopup(FloatLayout):
            pass

        popup = Popup(title="Modyfikowanie stanow", content=StatePopup(), size_hint=(None, None), size=(400, 400))
        popup.open()

    def change_state_diagram(self):
        # TODO
        # Implement a window allowing to change the state_diagram
        class DiagramPopup(FloatLayout):
            pass

        popup = Popup(title="Modyfikowanie diagramu", content=DiagramPopup(), size_hint=(None, None), size=(400, 400))
        popup.open()


class TuringGUI(App):
    def build(self):
        return TuringLayout()


TuringGUI().run()
