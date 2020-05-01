class TuringMachine:
    def __init__(self, alphabet, tape, state_list):
        self.alphabet = alphabet  # first symbol in alphabet is default empty symbol
        self.tape = tape
        self.state_list = state_list  # first state is the default starting state

        self.state_diagram = {}
        self.head_position = 0
        self.current_state = 0

        self.check_input_data()

    def check_input_data(self):

        # alphabet should have at least one symbol
        if len(self.alphabet) == 0:
            raise RuntimeError("Insufficient number of symbols")

        # state_list should have at least one state
        if len(self.state_list) == 0:
            raise RuntimeError("Insufficient number of states")

        # check tape
        for cell in self.tape:
            if cell not in self.alphabet:
                raise RuntimeError("Unrecognized character on the tape")
        
    def move_head(self, direction: chr):
        pass

    def perform_operation(self, instruction: list):
        pass
