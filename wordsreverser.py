import string

class WordsReverser:

    def reverseWords(self, sentence):
        tmp = string.split(sentence)
        tmp.reverse()
        return ' '.join(tmp)

    def reverseSet(self, set):
        return map(self.reverseWords, set)

    def formatOutput(self, set, i = 1):
        if not len(set):
            return ''
        else:
            return 'Case #' + str(i) + ': ' + set[0] + "\n" + self.formatOutput(set[1:], i+1)
