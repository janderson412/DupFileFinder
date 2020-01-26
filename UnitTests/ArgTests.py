'''
Unit tests for argument parsing
'''

import unittest
from DupFileFinder import ParseArguments

class TestArgumentParser(unittest.TestCase):

    def test_verbose(self):
        arglist = ['-v']
        arguments = ParseArguments(args=arglist)
        self.assertTrue(arguments.verbose)

    def test_defaults(self):
        arglist = []
        arguments = ParseArguments(args=arglist)
        self.assertFalse(arguments.verbose)


if __name__ == '__main__':
    unittest.main()

