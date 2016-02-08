__author__ = 'Srinivas Avireddy'

import json
import re
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from collections import Counter


def extractWordsFromJson(filename):
    tokens = []
    wordCount = []
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
    wordCounter = Counter(tokens)
    for word in wordCounter:
        wordCount.append({"text": word, "size": wordCounter[word]})
    outputFile = open("/Users/joemanley/workspace/traces_220/wordCloud/data/data.json", "w")
    outputFile.write("var data = " + json.dumps(wordCount))
    outputFile.close()
    return tokens


if __name__ == '__main__':
    print extractWordsFromJson("../data/tweets.json")