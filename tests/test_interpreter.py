import unittest

import interpreter

class TestInterpreter(unittest.TestCase):

    def test_hello_world(self):
        with open(r'../hello_world.bf', 'r') as file:
            code = file.read()
        result = interpreter.run(code).rstrip()
        self.assertEqual(result, 'Hello World!')
