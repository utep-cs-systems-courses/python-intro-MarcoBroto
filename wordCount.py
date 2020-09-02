#! python2.7
import sys, re

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('File arguments not passed in')
        exit()
    file_in, file_out = sys.argv[1], sys.argv[2] if len(sys.argv) >= 3 else 'output.txt'

    try:
        words = dict()
        with open(file_in, 'r') as inputFile:
            for line in inputFile:
                for word in re.split('\W', line.lower()): # Parse out whitespace and punctuation
                    words[word] = words[word]+1 if word in words else 1
            del words[''] # Remove empty string from word dictionary

        # Alphabetically sort dictionary by keys and write keys and values to output file
        with open(file_out, 'w') as outputFile:
            for k, v in sorted(words.items()): outputFile.write('%s %d\n' % (k, v))
    except IOError as err: print(err)
