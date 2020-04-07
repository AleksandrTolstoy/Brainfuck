import os
import unittest

import compiler

class TestInterpreter(unittest.TestCase):

    def test_hello_world(self):
        with open(r'../hello_world.bf', 'r') as file:
            code = file.read()
        c_code = compiler.compile_to_c(code)
        name = 'hello_world.bf'.replace('.bf', '')
        c_file = f'{name}.c'
        with open(c_file, 'w') as f:
            f.write(c_code)

        os.system(f'cc {c_file} -o {name}.o')
        result = os.system(f'./{name}.o')
        self.assertEqual(result, 0)


