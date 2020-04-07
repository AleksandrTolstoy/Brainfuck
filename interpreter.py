import sys
from collections import deque
from typing import Dict


def create_map(code: str) -> Dict[int, int]:
    """Finds pairs of brackets in code

    key and values ​​- byte index in code
    """
    bracket_map = {}
    stack = deque()
    for pos, symbol in enumerate(code):
        if symbol == '[':
            stack.append(pos)
        elif symbol == ']':
            last_open_pos = stack.pop()
            bracket_map[pos] = last_open_pos
            bracket_map[last_open_pos] = pos

    if stack:
        raise ValueError('Unclosed [')
    return bracket_map


def run(code: str, mem_size: int = 30000):
    """Executes code

    memory: program RAM
    data_ptr: current memory index
    instr_ptr: index of the current code instruction
    """
    memory = [0] * mem_size
    data_ptr = 0
    instr_ptr = 0
    bracket_map = create_map(code)

    output = ''
    while instr_ptr < len(code):
        command = code[instr_ptr]

        if command == '+':
            memory[data_ptr] += 1
        elif command == '-':
            memory[data_ptr] -= 1
        elif command == '>':
            data_ptr = (data_ptr + 1) % mem_size  # cyclic memory
        elif command == '<':
            data_ptr = (data_ptr - 1) % mem_size  # cyclic memory
        elif command == '.':
            output += chr(memory[data_ptr])
        elif command == ',':
            inp = input()
            memory[data_ptr] = ord(inp[0]) if inp else 0
        elif command == '[':
            if not memory[data_ptr]:
                instr_ptr = bracket_map[instr_ptr]
        elif command == ']':
            if memory[data_ptr]:
                instr_ptr = bracket_map[instr_ptr]

        instr_ptr += 1
    return output


if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as f:
            code = f.read()
        run(code)
    else:
        print(f'Usage: python3 {sys.argv[0]} <file_name>.bf')