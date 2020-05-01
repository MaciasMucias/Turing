

# Turing(Alphabet, Tape, State list):

-Alphabet = Alphabet      -> list of acceptable chars

-Tape = Tape              -> list of chars from Alphabet

-State list = State list  -> a list of states

-State diagram = {}       -> dictionary of dictionaries

-Head position = 0        -> a uint value

-Current state = 0        -> a uint value


# Methods:

-Check input data(Alphabet, Tape)                  -> checks if Tape is consisting of only Alphabet chars

-Move head(char)                                   -> moves head to left or right

-Perform operation(State diagram, Current state)   -> modifies current state and tape based on state diagram

-Run(Tape, Head position, State list, Current state, State diagram) -> Simulate the actions based on tape data



# State diagram example

{state:{char:[char, state, 'L'/'R']}}
