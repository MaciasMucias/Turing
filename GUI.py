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
    default_button = ObjectProperty(None)
    add_error_msg = ObjectProperty(None)
    del_error_msg = ObjectProperty(None)

    def __init__(self, names, add_function, remove_function, error_msg, length_check, **kwargs):
        super(ModifyElementsPopup, self).__init__(**kwargs)

        self.chr_list = names
        self.add_function = add_function
        self.remove_function = remove_function
        self.error_msg = error_msg
        self.length_check = length_check
        self.popup_id = 0

        self.alphabet = ElementsDD(names)

        self.update_button()

    def update_button(self):
        if len(self.chr_list) == 0:
            self.default_button.text = ""
        else:
            self.default_button.text = self.chr_list[0]

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

        self.update_button()
        MainGUI.main_layout.update_tape_buttons()

    def del_chr(self):
        self.add_error_msg.text = ""
        self.del_error_msg.text = ""

        if len(self.del_button.text) > 0:
            if self.chr_list == turing.alphabet:
                default = self.chr_list[0]
                if default == self.del_button.text:
                    if len(self.chr_list) == 1:
                        default = None
                    else:
                        default = self.chr_list[1]

                for i in range(len(turing.tape)):
                    if turing.tape[i] == self.del_button.text:
                        turing.tape[i] = default
                if default is None:
                    turing.tape = []

            self.remove_function(self.del_button.text)
            self.alphabet.update()
        else:
            self.del_error_msg.text = self.error_msg[2]

        self.del_button.text = ""

        self.update_button()
        MainGUI.main_layout.update_tape_buttons()

    def update_default(self, pos):
        i = 0
        while turing.tape[i] == self.chr_list[0]:
            turing.tape[i] = self.chr_list[pos]
            i += 1
            if i >= len(turing.tape):
                break

        i = len(turing.tape) - 1
        while turing.tape[i] == self.chr_list[0]:
            turing.tape[i] = self.chr_list[pos]
            i -= 1
            if i < 0:
                break

    def set_default(self):
        if self.default_button.text != "":
            pos = self.chr_list.index(self.default_button.text)

            # change empty symbols at the beginning and the end of the tape

            # this is bad but it works for now
            if self.chr_list == turing.alphabet:
                self.update_default(pos)
            self.chr_list[0], self.chr_list[pos] = self.chr_list[pos], self.chr_list[0]
            MainGUI.main_layout.update_tape_buttons()

    def open_DD(self, root, popup):
        self.popup_id = popup
        self.alphabet.open(root)

    def del_button_text(self, text):
        if self.popup_id == 1:
            self.del_button.text = text
        elif self.popup_id == 2:
            self.default_button.text = text


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
            MainGUI.main_layout.update_tape_buttons()
            if not result:
                self.add_diagram_msg.text = "Instruction already in the Diagram!"


class DeleteDiagramPopup(FloatLayout):
    in_symbol = ObjectProperty(None)
    in_state = ObjectProperty(None)
    out_symbol = ObjectProperty(None)
    out_state = ObjectProperty(None)
    out_direction = ObjectProperty(None)

    in_symbol_msg = ObjectProperty(None)
    in_state_msg = ObjectProperty(None)
    del_diagram_msg = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(DeleteDiagramPopup, self).__init__(**kwargs)

        self.in_symbols = ElementsDD([])
        self.in_states = ElementsDD(turing.state_diagram.keys())

        self.dropdown_active = 0

    def open_in_symbols(self, root):
        self.in_symbol_msg.text = ""
        self.dropdown_active = 1
        self.in_symbols.open(root)

    def open_in_states(self, root):
        self.in_state_msg.text = ""
        self.dropdown_active = 2
        self.in_states.open(root)

    def del_button_text(self, text):
        self.in_symbol.text = ""
        self.out_symbol.text = ""
        self.out_state.text = ""
        self.out_direction.text = ""

        if self.dropdown_active == 1:
            self.in_symbol.text = text
            self.out_symbol.text = turing.state_diagram[self.in_state.text][text][0]
            self.out_state.text = turing.state_diagram[self.in_state.text][text][1]
            self.out_direction.text = turing.state_diagram[self.in_state.text][text][2]
        elif self.dropdown_active == 2:
            self.in_state.text = text
            self.in_symbols._buttons = turing.state_diagram[text].keys()

    def del_diagram(self):
        good = True
        self.in_symbol_msg.text = ""
        self.in_state_msg.text = ""
        self.del_diagram_msg.text = ""
        if self.in_symbol.text == "":
            self.in_symbol_msg.text = "Choose a Symbol!"
            good = False
        if self.in_state.text == "":
            self.in_state_msg.text = "Choose a State!"
            good = False

        self.out_symbol.text = ""
        self.out_state.text = ""
        self.out_direction.text = ""

        if good:
            result = turing.diagram_del(self.in_state.text,
                                        self.in_symbol.text)
            self.in_symbol.text = ""
            self.in_state.text = ""
            self.in_states._buttons = turing.state_diagram.keys()
            self.in_symbols._buttons = []
            MainGUI.main_layout.update_tape_buttons()
            if not result:
                self.del_diagram_msg.text = "Instruction not in the Diagram!"


class SettingsPopoup(FloatLayout):
    def save(self):
        turing.save_data('saved.mach')

    def load(self):
        turing.load_data('saved.mach')
        MainGUI.main_layout.update_tape_buttons()
        MainGUI.main_layout.reset_turing()


class TuringLayout(FloatLayout):
    symbol_in = ObjectProperty(None)
    state_in = ObjectProperty(None)
    symbol_out = ObjectProperty(None)
    state_out = ObjectProperty(None)
    direction_out = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(TuringLayout, self).__init__(**kwargs)

        self.drop = ElementsDD(turing.alphabet)
        self.dropdown_active = 0

        self.num_buttons = 25
        self.active_button = 0
        self.buttons = []
        self.first_position_displayed = 0  # which cell from the tape is displayed on the leftmost button
        for i in range(self.num_buttons):
            self.buttons.append(Button(size_hint=(1/self.num_buttons, 1/20),
                                       pos_hint={"x": 1/self.num_buttons*i, "top": 0.8}))
            self.buttons[-1].button_pos = i

            self.buttons[-1].bind(on_press=self.dismiss_drop)
            self.buttons[-1].bind(on_release=self.open_drop)
            self.add_widget(self.buttons[-1])

        self.popup_class = self
        self.update_tape_buttons()
        self.update_active_cell()

    def update_active_cell(self):
        for button in self.buttons:
            button.background_color = (0.75, 0.75, 0.75, 1)

        self.buttons[self.active_button].background_color = (0, 1, 0, 1)

    def run_turing(self):
        while turing.perform_operation():
            continue

        self.move_active_cell(turing.head_position - (self.first_position_displayed+self.active_button))

    def reset_turing(self):
        turing.current_state = 0
        self.show_info()

    def turing_step(self):
        turing.perform_operation()
        self.move_active_cell(turing.head_position - (self.first_position_displayed + self.active_button))

    def move_active_cell(self, pos):
        if not turing.tape:
            return
        self.active_button += pos
        if self.active_button < 0:
            new_pos = self.first_position_displayed+self.active_button
            self.first_position_displayed = turing.new_position(new_pos)
            self.active_button = 0
        elif self.active_button >= self.num_buttons:
            new_pos = self.first_position_displayed + self.active_button - self.num_buttons + 1
            self.first_position_displayed = turing.new_position(new_pos)
            self.active_button = self.num_buttons - 1
        turing.head_position = self.first_position_displayed+self.active_button
        self.update_active_cell()
        self.update_tape_buttons()

    def show_info(self):
        symbol = state = None

        if turing.tape:
            symbol = turing.tape[turing.head_position]

        if turing.current_state is not None and turing.state_list:
            state = turing.state_list[turing.current_state]

        self.symbol_in.text = symbol if symbol is not None else 'None'
        self.state_in.text = state if state is not None else 'None'

        if state not in turing.state_diagram:
            self.symbol_out.text = "None"
            self.state_out.text = "None"
            self.direction_out.text = "None"
            return

        if symbol not in turing.state_diagram[state]:
            self.symbol_out.text = "None"
            self.state_out.text = "None"
            self.direction_out.text = "None"
            return

        instruction = turing.state_diagram[state][symbol]
        self.symbol_out.text = instruction[0]
        self.state_out.text = instruction[1]
        self.direction_out.text = instruction[2]

    def del_button_text(self, text):
        self.buttons[self.dropdown_active].text = text
        turing.tape[turing.new_position(self.first_position_displayed + self.dropdown_active)] = text
        self.show_info()

    def open_drop(self, instance):
        self.dropdown_active = instance.button_pos
        self.drop.open(instance)

    def dismiss_drop(self, instance):
        self.drop.dismiss()

    def dismissed_popup(self, instance):
        self.popup_class = self

    def update_tape_buttons(self):
        self.drop._buttons = turing.alphabet
        if len(turing.alphabet) == 0:
            for button in self.buttons:
                button.text = ""
            return
        for i, button in enumerate(self.buttons):
            button.text = turing.tape[turing.new_position(i + self.first_position_displayed)]

        self.show_info()

    def change_alphabet(self):
        error_msg = ["Symbol already in Alphabet!",
                     "Symbol have to be a single character!",
                     "Choose a symbol to delete from Alphabet!"]
        self.popup_class = ModifyElementsPopup(names=turing.alphabet, add_function=turing.alphabet_add,
                                               remove_function=turing.alphabet_remove, error_msg=error_msg,
                                               length_check=lambda x: len(x) == 1)
        popup = Popup(title="Modify Alphabet", title_align="center", content=self.popup_class,
                      size_hint=(None, None), size=(400, 400))
        popup.bind(on_dismiss=self.dismissed_popup)
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
        popup.bind(on_dismiss=self.dismissed_popup)
        popup.open()

    def change_state_diagram(self):
        self.popup_class = DiagramPopup()
        popup = Popup(title="Add Instruction", title_align="center", content=self.popup_class,
                      size_hint=(None, None), size=(800, 400))
        popup.bind(on_dismiss=self.dismissed_popup)
        popup.open()

    def del_state_diagram(self):
        self.popup_class = DeleteDiagramPopup()
        popup = Popup(title="Delete Instruction", title_align="center", content=self.popup_class,
                      size_hint=(None, None), size=(800, 400))
        popup.bind(on_dismiss=self.dismissed_popup)
        popup.open()

    def settings(self):
        self.popup_class = SettingsPopoup()
        popup = Popup(title="Settings", title_align="center", content=self.popup_class,
                      size_hint=(None, None), size=(400, 400))
        popup.bind(on_dismiss=self.dismissed_popup)
        popup.open()


class TuringGUI(App):
    main_layout = None

    def build(self):
        self.main_layout = TuringLayout()
        return self.main_layout


MainGUI = TuringGUI()

MainGUI.run()



