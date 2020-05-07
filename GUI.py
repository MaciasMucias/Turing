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
from kivy.factory import Factory

# Window.fullscreen = 'auto'

turing = TuringMachine()


class AlphabetDD(Factory.DropDown):
    def __init__(self, **kwargs):
        super(AlphabetDD, self).__init__(**kwargs)
        self._buttons = turing.alphabet
        self._filter = Factory.TextInput(size_hint_y=None, height='40dp', multiline=False)
        self.add_widget(self._filter)
        self._filter.bind(text=self.apply_filter)

    def update(self):
        self._buttons = turing.alphabet
        print(self._buttons)

    def open(self, root):
        super().open(root)
        self.clear_widgets()
        self.add_widget(self._filter)
        for btn in self._buttons:
            self.add_widget(Factory.FDDButton(text=btn))

    def apply_filter(self, wid, value):
        self.clear_widgets()
        self.add_widget(self._filter)
        for btn in self._buttons:
            if not value or value in btn:
                self.add_widget(Factory.FDDButton(text=btn, obj=self))


class AlphabetPopup(FloatLayout):
    new_chr = ObjectProperty(None)
    del_button = ObjectProperty(None)
    add_error_msg = ObjectProperty(None)
    del_error_msg = ObjectProperty(None)
    chr_list = turing.alphabet

    alphabet = AlphabetDD()

    def add_chr(self):
        self.add_error_msg.text = ""
        self.del_error_msg.text = ""

        if len(self.new_chr.text) == 1:
            if not turing.alphabet_add(self.new_chr.text):
                self.add_error_msg.text = "Symbol already in Alphabet!"
            self.alphabet.update()
        else:
            self.add_error_msg.text = "Symbol have to be a single character!"
        self.new_chr.text = ""

    def del_chr(self):
        self.add_error_msg.text = ""
        self.del_error_msg.text = ""

        if len(self.del_button.text) > 0:
            turing.alphabet_remove(self.del_button.text)
            self.alphabet.update()
        else:
            self.del_error_msg.text = "Choose a symbol to delete from Alphabet!"

        self.del_button.text = ""

    def open_DD(self, root):
        self.alphabet.open(root)

    def del_button_text(self, text):
        self.del_button.text = text


class TuringLayout(FloatLayout):
    popup_class = None

    def change_alphabet(self):
        # TODO
        # Implement UI inside the popup allowing change the alphabet
        self.popup_class = AlphabetPopup()
        popup = Popup(title="Modify Alphabet", title_align="center", content=self.popup_class,
                      size_hint=(None, None), size=(400, 400))
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
    main_layout = None

    def build(self):
        self.main_layout = TuringLayout()
        return self.main_layout


MainGUI = TuringGUI()

MainGUI.run()



