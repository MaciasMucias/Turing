class TuringMachine:
    def __init__(self, alphabet, tape, state_list):
        self.alphabet = alphabet
        self.tape = tape
        self.state_list = state_list

        self.state_diagram = {}
        self.head_position = 0
        self.current_state = 0

        self.check_input_data()

    def check_input_data(self):
        pass

    def move_head(self, direction: chr):
        pass

    def perform_operation(self, instruction: list):
        pass
