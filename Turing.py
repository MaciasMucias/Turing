class TuringMachine:
    def __init__(self, alphabet: list, tape: list, state_list: list, state_diagram: dict):
        self.alphabet = alphabet  # first symbol in alphabet is default empty symbol
        self.tape = tape
        self.state_list = state_list  # first state is the default starting state

        self.state_diagram = state_diagram
        self.head_position = 0
        self.current_state = 0

        self.check_input_data()

    def check_state_diagram(self):
        if not type(self.state_diagram) is dict:
            raise RuntimeError("State Diagram is not a dictionary")

        # go through all states in state_diagram
        for state in self.state_diagram.keys():
            if state not in self.state_list:
                raise RuntimeError("Invalid state value")

            if not type(self.state_diagram[state]) is dict:
                raise RuntimeError("Invalid type of element in state_diagram")

            # go through all symbols in each state
            for symbol in self.state_diagram[state].keys():
                if symbol not in self.alphabet:
                    raise RuntimeError("Invalid symbol value")

                instruction = self.state_diagram[state][symbol]
                if not type(instruction) is list:
                    raise RuntimeError("Instruction is not a list")

                if len(instruction) != 3:
                    raise RuntimeError("Incorrect length of instruction")

                # elements of instruction: symbol (in alphabet); state (in state_list); direction (L or R)
                if instruction[0] not in self.alphabet or instruction[1] not in self.state_diagram or \
                        instruction[2] not in ['L', 'R']:
                    raise RuntimeError("Invalid values in instruction")

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

        self.check_state_diagram()

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

    def perform_operation(self):
        state_val = self.state_list[self.current_state]
        symbol_val = self.tape[self.head_position]

        if state_val not in self.state_diagram:
            return False  # end of program
        if symbol_val not in self.state_diagram[state_val]:
            return False  # end of program

        instruction = self.state_diagram[state_val][symbol_val]

        self.tape[self.head_position] = instruction[0]
        self.current_state = self.state_list.index(instruction[1])
        self.move_head(instruction[2])

        return True

    def alphabet_add(self, symbol: chr):
        if symbol in self.alphabet:
            return False

        self.alphabet.append(symbol)
        return True

    def alphabet_remove(self, symbol: chr):
        if symbol not in self.alphabet:
            return False

        self.alphabet.remove(symbol)
        return True

    def state_add(self, state: str):
        if state in self.state_list:
            return False

        self.state_list.append(state)
        return True

    def state_remove(self, state: str):
        if state not in self.state_list:
            return False

        self.state_list.remove(state)
        return True
