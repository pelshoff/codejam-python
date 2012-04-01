import unittest
from wordsreverser import WordsReverser

class WordReverserTest(unittest.TestCase):

    def setUp(self):
        self.reverser = WordsReverser()

    def testReverseWords(self):
        self.assertEqual('3 2 1', self.reverser.reverseWords('1 2 3'))

    def testReverseSet(self):
        self.assertEqual(['3 2 1', 'c b a'], self.reverser.reverseSet(['1 2 3', 'a b c']))

    def testFormatOutput(self):
        expected = '''Case #1: 3 2 1
Case #2: c b a
'''
        self.assertEqual(expected, self.reverser.formatOutput(['3 2 1', 'c b a']))

if __name__ == '__main__':
    unittest.main()