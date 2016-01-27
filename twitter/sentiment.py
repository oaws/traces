import sys
import json
from pprint import pprint

def main():
	
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    afinnfile = open(sys.argv[1])
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  
        scores[term] = int(score)  

	new=open(sys.argv[2])
    for line in new:
        data=json.loads(line)
        sum=0
        if "text" in data:
	    l=data["text"]
            l2=l.encode('ascii','ignore')
            ter=l2.split(" ")
            for a in ter:
                if a in scores:
                    sum=sum+scores.get(a)
            print sum          

if __name__ == '__main__':
    main()