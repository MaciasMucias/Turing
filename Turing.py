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

        if not type(self.alphabet) is list:
            raise RuntimeError("Alphabet is not a list")

        if not type(self.state_list) is list:
            raise RuntimeError("State List is not a list")

        if not type(self.tape) is list:
            raise RuntimeError("Tape is not a list")

        # alphabet should have at least one symbol
        if self.alphabet:
            raise RuntimeError("Insufficient number of symbols")

        # state_list should have at least one state
        if self.state_list:
            raise RuntimeError("Insufficient number of states")

        # tape should have at least one cell
        if self.tape:
            raise RuntimeError("Insufficient number of cells")

        # check tape
        for cell in self.tape:
            if cell not in self.alphabet:
                raise RuntimeError("Unrecognized character on the tape")

    def move_head(self, direction: chr):  # direction: L -> left, R -> right
        if direction == "L":
            # add empty symbols if at the start
            if self.head_position == 0:
                self.tape.insert(0, self.alphabet[0])
            else:
                self.head_position -= 1

        elif direction == "R":
            self.head_position += 1
            # add empty symbols if at the end
            if self.head_position == len(self.tape):
                self.tape.append(self.alphabet[0])

    def perform_operation(self, instruction: list):
        pass
