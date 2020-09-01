#! python2.7
import sys
import re

def countWordsInFile(fileName):
    try: file = open(fileName, 'r')
    except FileNotFoundError: raise FileNotFoundError()
    except IOError: raise IOError()
    
    # Parse out whitespace and punctuation
    words = dict()
    for line in file:
        for word in re.split('[\W\s]*', line):
            words[word] = words[word]+1 if word in words else 1
    del words['']

    for k, v in sorted(words.items(), key=lambda x: x[1]): print k, v

def main():
    for i in range(1, len(sys.argv)):
        param = sys.argv[i]
        if type(param) is str:
            try: countWordsInFile(param)
            except Exception as err: print(err)
        else:
            raise FileNotFoundError()

if __name__ == "__main__": main()
