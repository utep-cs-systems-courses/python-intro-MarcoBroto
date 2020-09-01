#! python2.7
import sys
import re

def countWordsInFile(inputFileName, outputFileName):
    # Find and load input and output files
    inputFile = open(inputFileName, 'r')
    outputFile = open(outputFileName, 'w')
    
    # Parse out whitespace and punctuation
    words = dict()
    for line in inputFile:
        for word in re.split('[\W\s]*', line):
            words[word] = words[word]+1 if word in words else 1
    del words[''] # Remove empty string from word dictionary

    # Sort words by ascending frequency and write stats to output file
    for k, v in sorted(words.items(), key=lambda x: x[1]): outputFile.write('%s %d\n' % (k, v))

def main():
    if len(sys.argv) < 2:
        print('File arguments not passed in')
        return
    
    # Assign input and ouput file names from CL arguments
    file_in = sys.argv[1]
    file_out = sys.argv[2] if len(sys.argv) >= 3 else 'output.txt'

    try: countWordsInFile(file_in, file_out)
    except IOError as err: print(err)

if __name__ == "__main__": main()
