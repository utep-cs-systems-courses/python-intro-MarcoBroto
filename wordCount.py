#! python2.7
import sys
import re

def countWordsInFile(inputFileName, outputFileName):
    # Load input and output files
    inputFile = open(inputFileName, 'r')
    outputFile = open(outputFileName, 'w')
    
    # Parse out whitespace and punctuation
    words = dict()
    for line in inputFile:
        for word in re.split('\W', line.lower()):
            words[word] = words[word]+1 if word in words else 1
    del words[''] # Remove empty string from word dictionary

    # Alphabetically sort dictionary by keys and write keys and values to output file
    for k, v in sorted(words.items()): outputFile.write('%s %d\n' % (k, v))

def main():
    if len(sys.argv) < 2:
        print('File arguments not passed in')
        return
    
    # Assign input and output file names from CL arguments
    file_in = sys.argv[1]
    file_out = sys.argv[2] if len(sys.argv) >= 3 else 'output.txt'

    try: countWordsInFile(file_in, file_out)
    except IOError as err: print(err.with_traceback())

if __name__ == "__main__": main()
