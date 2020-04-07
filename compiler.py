import sys
import os

INTRODUCTION = """#include <string.h> 
#include <stdio.h>
int main() {
    const int mem_size = 30000;
    char mem[mem_size];
    memset(mem, 0, mem_size);
    int cur = 0;
"""

ENDING = """
    return 0;
}
"""


def compile_to_c(code: str) -> str:
    """Turns Brainfuck commands into C code"""
    instr_ptr = 0

    bias = 4
    c_code = INTRODUCTION

    for command in code:
        content = ''
        if command == '+':
            content = 'mem[cur]++;'
        elif command == '-':
            content = 'mem[cur]--;'
        elif command == '>':
            content = 'cur++;'
        elif command == '<':
            content = 'cur--;'
        elif command == '.':
            content = 'putchar(mem[cur]);'
        elif command == ',':
            content = 'mem[cur] = getchar();'
        elif command == '[':
            content = 'while(mem[cur]) {'
        elif command == ']':
            content = '}'

        instr_ptr += 1
        # need for a pretty output
        if content:
            if command == ']':
                bias -= 4
            c_code += ' ' * bias + content + '\n'
            if command == '[':
                bias += 4

    c_code += ENDING
    return c_code


if __name__ == '__main__':
    if len(sys.argv) == 2:
        name = sys.argv[1]
        with open(name, 'r') as f:
            code = f.read()
        c_code = compile_to_c(code)

        name = name.replace('.bf', '')
        c_file = f'{name}.c'
        with open(c_file, 'w') as f:
            f.write(c_code)

        os.system(f'cc {c_file} -o {name}.o')
        os.system(f'./{name}.o')
    else:
        print(f'Usage: python3 {sys.argv[0]} <file_name>.bf')