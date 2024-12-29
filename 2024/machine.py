'This module implements the stack machine that is used to execute instructions.'

class Instr:
    '''Base class for instructions.'''

    def Execute(self, state):
        '''The Execute() method should be implemented by all subclasses.
           It operates on the machine state, and return a value, or None
           to indicate that execution should continue.'''
        raise NotImplementedError()


class PushInstr(Instr):
    '''The `push` instruction pushes a value on the stack.'''

    def __init__(self, op):
        self.op = op

    def Execute(self, state):
        state.stack.append(self.op(state))


class AddInstr(Instr):
    '''The `add` instruction takes two values from the top of the stack,
       and replaces them with their sum.'''

    def Execute(self, state):
        stack = state.stack
        stack.append(stack.pop() + stack.pop())


class JmposInstr(Instr):
    '''The `jmpos` instruction takes a value off the stack, and adds an offset
       to the instruction pointer if the value was nonnegative.'''

    def __init__(self, offset):
        self.offset = offset

    def Execute(self, state):
        if state.stack.pop() >= 0:
            state.ip += self.offset


class RetInstr(Instr):
    '''The `ret` instruction returns the value at the top of the stack.'''

    def Execute(self, state):
        return state.stack.pop()



class State:
    '''Represents the state of a running machine.'''
    def __init__(self, instructions, x, y, z):
        self.instructions = instructions
        self.x = x
        self.y = y
        self.z = z
        self.ip = 0
        self.stack = []

    def Execute(self):
        result = None       
        while result is None:
            instr = self.instructions[self.ip]
            self.ip += 1
            result = instr.Execute(self)
        return result


def ParseOperand(op):
    '''Parses an operand (only used for the `push` instruction in this problem),
       which can either reference the x, y or z register, or contain an
       immediate integer value.'''

    if op == 'x':
        return lambda state: state.x

    if op == 'y':
        return lambda state: state.y

    if op == 'z':
        return lambda state: state.z

    val = int(op)
    return lambda unused_state: val


def ParseInstruction(line):
    '''Parses a string into an Instruction instance.'''

    # The problem statement uses lowercase, but input data uses uppercase
    # operands. I'll convert the entire line to lowercase, effectively making
    # the parser case insensitive.
    parts = line.lower().split()

    if len(parts) == 1:
        if parts[0] == 'add':
            return AddInstr()

        if parts[0] == 'ret':
            return RetInstr()

    if len(parts) == 2:
        if parts[0] == 'push':
            return PushInstr(ParseOperand(parts[1]))

        if parts[0] == 'jmpos':
            return JmposInstr(int(parts[1]))

    raise ValueError(f'Unrecognized instruction')


class Program:
    '''Represents a parsed program, without associated state.'''

    def __init__(self, file):
        '''Initializes the program by reading instructions from the given file.'''
        self.instructions = [ParseInstruction(line) for line in file]

    def Execute(self, x, y, z):
        '''Executes the entire program starting with the given register values,
           and returns the value returned by the final `ret` instruction.'''
        return State(self.instructions, x, y, z).Execute()
