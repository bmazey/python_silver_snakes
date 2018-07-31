from src.WordList import *
import unittest


class TestClass(unittest.TestCase):

    def test_swear_word_count(self):
        wordlist = WordList()

        self.assertEqual(wordlist.swear_word_count("hey hey hey arse ass"), 2)
        self.assertEqual(wordlist.swear_word_count("hey hey hey ugefv"), 0)
        self.assertEqual(wordlist.swear_word_count("asshi"), 0)


if __name__ == '__main__':
    unittest.main()