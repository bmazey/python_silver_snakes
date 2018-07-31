from src.WordList import *
import unittest


class TestClass(unittest.TestCase):

    def test_adding_word(self):
        wordlist = WordList()
        wordlist.add('ha')
        self.assertEqual(wordlist.list[-1], 'ha')


if __name__ == '__main__':
    unittest.main()
