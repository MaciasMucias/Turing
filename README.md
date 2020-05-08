# Turing Machine Simulator
Simulates how the Turing Machine works.

## Class Turing(alphabet, tape, state_list, state_diagram)

  **Variables**

  * **alphabet**        -> list of acceptable characters (later called _Symbols_)

  * **tape**            -> list of _Symbols_

  * **state_list**      -> list of acceptable states of the machine (later called _States_)

  * **state_diagram**   -> dictionary of dictionaries where the first key is _State_, second is _Symbol_ and each entry is an instruction for the machine

  * **head_position**   -> position on Tape (0 initially)

  * **current_state**   -> state of the machine (0 initially)

  **Methods**

  * **check_input_data(self)**        -> checks if **alphabet**, **tape** and **state_list** are valid

  * **check_state_diagram(self)**     -> checks if **state_diagram** is valid

  * **move_head(self, direction)**    -> modifies **head_position**; moves head left (if **direction** == "L") or right (if **direction** == "R")

  * **perform_operation(self)**       -> modifies **current_state** and **tape** based on the instruction in **state_diagram**

  * **alphabet_add(self, symbol)**    -> adds new _Symbol_ to **alphabet**

  * **alphabet_remove(self, symbol)** -> removes _Symbol_ from **alphabet**

  * **state_add(self, state)**        -> adds new _State_ to **state_list**

  * **state_remove(self, state)**     -> removes _State_ from **state_list**

  **State diagram example**
    
   {_State_: {_Symbol_: [_Symbol_, _State_, 'L' or 'R']}}
