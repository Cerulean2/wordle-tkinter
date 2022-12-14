import random

def readWholeFile():
    with open('words.txt') as f:
        lines = f.readlines()

    return lines 

words = readWholeFile()
listLen = len(words)

randomNum = random.randint(0, listLen)
