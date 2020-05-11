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

turing = TuringMachine()


class ElementsDD(Factory.DropDown):
    def __init__(self, button_names, **kwargs):
        super(ElementsDD, self).__init__(**kwargs)
        self._buttons = button_names
        self._filter = Factory.TextInput(size_hint_y=None, height='40dp', multiline=False)
        self.add_widget(self._filter)
        self._filter.bind(text=self.apply_filter)

    def update(self):
        self._buttons = self._buttons

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
                self.add_widget(Factory.FDDButton(text=btn))


class ModifyElementsPopup(FloatLayout):
    new_chr = ObjectProperty(None)
    del_button = ObjectProperty(None)
    add_error_msg = ObjectProperty(None)
    del_error_msg = ObjectProperty(None)

    def __init__(self, names, add_function, remove_function, error_msg, length_check, **kwargs):
        super(ModifyElementsPopup, self).__init__(**kwargs)

        self.chr_list = names
        self.add_function = add_function
        self.remove_function = remove_function
        self.error_msg = error_msg
        self.length_check = length_check

        self.alphabet = ElementsDD(names)

    def add_chr(self):
        self.add_error_msg.text = ""
        self.del_error_msg.text = ""

        if self.length_check(self.new_chr.text):
            if not self.add_function(self.new_chr.text):
                self.add_error_msg.text = self.error_msg[0]
            self.alphabet.update()
        else:
            self.add_error_msg.text = self.error_msg[1]
        self.new_chr.text = ""

    def del_chr(self):
        self.add_error_msg.text = ""
        self.del_error_msg.text = ""

        if len(self.del_button.text) > 0:
            self.remove_function(self.del_button.text)
            self.alphabet.update()
        else:
            self.del_error_msg.text = self.error_msg[2]

        self.del_button.text = ""

    def open_DD(self, root):
        self.alphabet.open(root)

    def del_button_text(self, text):
        self.del_button.text = text


class DiagramPopup(FloatLayout):
    in_symbol = ObjectProperty(None)
    in_state = ObjectProperty(None)
    out_symbol = ObjectProperty(None)
    out_state = ObjectProperty(None)

    in_symbol_msg = ObjectProperty(None)
    in_state_msg = ObjectProperty(None)
    out_symbol_msg = ObjectProperty(None)
    out_state_msg = ObjectProperty(None)
    add_diagram_msg = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(DiagramPopup, self).__init__(**kwargs)

        self.in_symbols = ElementsDD(turing.alphabet)
        self.out_symbols = ElementsDD(turing.alphabet)
        self.in_states = ElementsDD(turing.state_list)
        self.out_states = ElementsDD(turing.state_list)

        self.direction = 0
        self.possible_directions = ['L', 'R']
        self.dropdown_active = 0

    def add_chr(self):
        self.add_error_msg.text = ""
        self.del_error_msg.text = ""
        '''
        if self.length_check(self.new_chr.text):
            if not self.add_function(self.new_chr.text):
                self.add_error_msg.text = self.error_msg[0]
            self.alphabet.update()
        else:
            self.add_error_msg.text = self.error_msg[1]
        self.new_chr.text = ""
        '''

    def del_chr(self):
        self.add_error_msg.text = ""
        self.del_error_msg.text = ""
        '''
        if len(self.del_button.text) > 0:
            self.remove_function(self.del_button.text)
            self.alphabet.update()
        else:
            self.del_error_msg.text = self.error_msg[2]

        self.del_button.text = ""
        '''

    def open_in_symbols(self, root):
        self.in_symbol_msg.text = ""
        self.dropdown_active = 1
        self.in_symbols.open(root)

    def open_out_symbols(self, root):
        self.out_symbol_msg.text = ""
        self.dropdown_active = 2
        self.out_symbols.open(root)

    def open_in_states(self, root):
        self.in_state_msg.text = ""
        self.dropdown_active = 3
        self.in_states.open(root)

    def open_out_states(self, root):
        self.out_state_msg.text = ""
        self.dropdown_active = 4
        self.out_states.open(root)

    def change_direction(self, root):
        self.direction = (self.direction + 1) % 2
        root.text = self.possible_directions[self.direction]

    def del_button_text(self, text):
        if self.dropdown_active == 1:
            self.in_symbol.text = text
        elif self.dropdown_active == 2:
            self.out_symbol.text = text
        elif self.dropdown_active == 3:
            self.in_state.text = text
        elif self.dropdown_active == 4:
            self.out_state.text = text

    def set_diagram(self):
        self.in_symbol_msg.text = ""
        self.out_symbol_msg.text = ""
        self.in_state_msg.text = ""
        self.out_state_msg.text = ""
        self.add_diagram_msg.text = ""
        good = True
        if self.in_symbol.text == "":
            self.in_symbol_msg.text = "Choose a Symbol!"
            good = False
        if self.in_state.text == "":
            self.in_state_msg.text = "Choose a State!"
            good = False
        if self.out_symbol.text == "":
            self.out_symbol_msg.text = "Choose a Symbol!"
            good = False
        if self.out_state.text == "":
            self.out_state_msg.text = "Choose a State!"
            good = False

        if good:
            result = turing.diagram_set(self.in_state.text,
                                        self.in_symbol.text,
                                        self.out_symbol.text,
                                        self.out_state.text,
                                        self.possible_directions[self.direction])

            if not result:
                self.add_diagram_msg.text = "Instruction already in the Diagram!"


class SettingsPopoup(FloatLayout):
    pass


class TuringLayout(FloatLayout):
    popup_class = None

    def change_alphabet(self):
        error_msg = ["Symbol already in Alphabet!",
                     "Symbol have to be a single character!",
                     "Choose a symbol to delete from Alphabet!"]
        self.popup_class = ModifyElementsPopup(names=turing.alphabet, add_function=turing.alphabet_add,
                                               remove_function=turing.alphabet_remove, error_msg=error_msg,
                                               length_check=lambda x: len(x) == 1)
        popup = Popup(title="Modify Alphabet", title_align="center", content=self.popup_class,
                      size_hint=(None, None), size=(400, 400))
        popup.open()

    def change_state_list(self):
        error_msg = ["State already in States' List!",
                     "State has to have at least one character!",
                     "Choose a state to delete from States' List!"]
        self.popup_class = ModifyElementsPopup(names=turing.state_list, add_function=turing.state_add,
                                               remove_function=turing.state_remove, error_msg=error_msg,
                                               length_check= lambda x: len(x) > 0)
        popup = Popup(title="Modify States' List", title_align="center", content=self.popup_class,
                      size_hint=(None, None), size=(400, 400))
        popup.open()

    def change_state_diagram(self):
        self.popup_class = DiagramPopup()
        popup = Popup(title="Modify States' Diagram", title_align="center", content=self.popup_class,
                      size_hint=(None, None), size=(800, 400))
        popup.open()

    def settings(self):
        self.popup_class = SettingsPopoup()
        popup = Popup(title="Settings", title_align="center", content=self.popup_class,
                      size_hint=(None, None), size=(400, 400))
        popup.open()


class TuringGUI(App):
    main_layout = None

    def build(self):
        self.main_layout = TuringLayout()
        return self.main_layout


MainGUI = TuringGUI()

MainGUI.run()



