import string
import sys
from wordsreverser import WordsReverser

def parseInput(inputString):
    input = string.split(inputString.strip(), "\n")
    return input[1:int(input[0])+1]

def reverseInput(inFile, outFile):
    reverser = WordsReverser()
    sentences = parseInput(open(inFile, 'r').read())
    output = reverser.formatOutput(reverser.reverseSet(sentences)).strip()
    open(outFile, 'w').write(output)

inFile = sys.argv[1]
outFile = inFile.replace('.in', '.out')
reverseInput(inFile, outFile)