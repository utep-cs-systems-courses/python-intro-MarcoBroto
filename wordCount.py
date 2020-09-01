#! python2.7
import sys
import re

def nextWord(file):
    for line in file: yield line

def countFileWords(fileName):
    try: file = open(fileName, 'r')
    except FileNotFoundError: raise FileNotFoundError()
    except IOError: raise IOError()
    words = dict()

    for line in (line for line in file):
        for word in re.split('[\W]*', line.lower()):
            words[word] = words[word]+1 if word in words else 1
    del words['']

if __name__ == "__main__":
    arg_len = len(sys.argv)
    for i in range(1, arg_len):
        param = sys.argv[i]
        if type(param) is str:
            try: countFileWords(param)
            except Exception as err: print(err)
        else: raise ValueError
