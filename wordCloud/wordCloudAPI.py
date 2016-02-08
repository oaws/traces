__author__ = 'Srinivas Avireddy'

import json
import re
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords


def extractWordsFromJson(filename):
    data = []
    tokens = []
    with open(filename) as dataFile:
        data = json.load(dataFile)
    for d in data:
        text = d['text']
        #data cleaning

        #removing punctuations
        letterOnly = re.sub("[^a-zA-Z]", " ", text)
        lowerCase = letterOnly.lower()

        #splitting words
        words = lowerCase.split()

        #lemmatizer for words
        lemmatizer = WordNetLemmatizer()
        words = [lemmatizer.lemmatize(w) for w in words if not w in stopwords.words("english")]

        #Adding words to the list of tokens
        tokens.extend(words)
    return tokens


if __name__ == '__main__':
    print extractWordsFromJson("tweets.json")

