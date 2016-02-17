__author__ = 'Srinivas Avireddy'

"""

To do: i) replace strings "" / ''
       ii) remove numbers
       iii)

"""

from collections import defaultdict
import os
import keyword
import nltk
from nltk import word_tokenize

bagOfWords = defaultdict(int)

def findBagOfWords(document):
    global bagOfWords
    f = open(document,"r")
    tokens = word_tokenize(f.read())
    #print "came here"
    print tokens
    f.close()
    print len(bagOfWords)
    return


def parseDirectory(directory):
        if len(bagOfWords) >= 10000:
            print bagOfWords
            return
        files=os.listdir(directory)
        for fl in files:
            path=os.path.join(directory,fl)
            if os.path.isdir(path):
                parseDirectory(path)
            else:
                filename, fileExtension = os.path.splitext(path)
                validFileExtensions = [".py",".java",".c",".cpp"]
                if fileExtension in validFileExtensions:
                    print "came here"
                    findBagOfWords(path)
        return

if __name__ == "__main__":
    parseDirectory("/Users/maheshwar/PycharmProjects")
    #print keyword.kwlist
print bagOfWords


