from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.factory import Factory

Builder.load_string('''
<FDDButton@Button>:
    size_hint_y: None
    height: '50dp'

<FilterDD>:
    auto_dismiss: False
''')


class FilterDD(Factory.DropDown):
    def __init__(self, buttons, **kwargs):
        super(FilterDD, self).__init__(**kwargs)
        self._buttons = buttons
        self._filter = filter = Factory.TextInput(size_hint_y=None)
        self.add_widget(filter)
        filter.bind(text=self.apply_filter)
        self.apply_filter(None, '')

        # You need this to add widgets here for apply_filter2:
        # for text in buttons:
        #    self.add_widget(Factory.FDDButton(text=text))

    def apply_filter(self, wid, value):
        self.clear_widgets()
        self.add_widget(self._filter)
        for btn in self._buttons:
            if not value or value in btn:
                self.add_widget(Factory.FDDButton(text=btn))

    def apply_filter2(self, wid, value):
        if not value:
            return
        for btn in self.container.children[:-1]:  # skip textinput
            if value in btn.text:
                self.scroll_to(btn)
                break


fdd = FilterDD(["one", "two", "three", "four", "five", "six",
                "seven", "eight", "nine", "ten"])

runTouchApp(Builder.load_string('''
#:import fdd __main__.fdd

Button:
    size_hint: None, None
    pos: 200, 200
    on_press:
        fdd.open(self)
'''))