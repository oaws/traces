__author__ = 'Srinivas Avireddy'


def symbolToNumber(symbol):
    if symbol == "A":
        return 0
    elif symbol == "C":
        return 1
    elif symbol == "G":
        return 2
    else:
        return 3

def patternToNumber(pattern):
    if len(pattern) == 0:
        return 0
    symbol = pattern[len(pattern)-1]
    prefix = pattern[0:len(pattern)-1]
    return 4 * patternToNumber(prefix) + symbolToNumber(symbol)


def computeFrequencyArray(text,k):
    frequencyArray = [0] * pow(4,k)
    for i in xrange(0,len(text)-k+1):
        pattern = text[i:i+k]
        j = patternToNumber(pattern)
        frequencyArray[j] += 1
    return frequencyArray

#frequencyArray = computeFrequencyArray("ATCAGTGTATTCAACAGTCATTTGCGGCGATGCGGCTTGGTTTGAAAGTACCTTATCGAGAGAGTGTAGGCCGAGACCGGCTCGCCTTCCTAGAGGTGTGTGTATGGTGGGAAACTTAGTTCAGACCTAAGAATCGCCTAACTGGCACGGGCAACTGTACGAGGAGGAGCTACATCACAGGCTGTTCAGGGCGGACTCTGCACTCCACCGATGAAGCGAAGCCTTAGACCGTTGAGCCTGTGGAGGGTTAGTTCATACGAACTGTAAATGATACTTTGTCCAAGGGAGCCCCTGCTTTTTGATAAGCGCTCCGGGCTCGTAAGCTTGATGTTTCCCGGAATATAGGATGACCTAGAGATCTCGCGTGGAGCATAATAAACGCTTCGTATTGGTCGGCCTAGGCTTTTAAACCTAGATTCTGACTAGTATGGTTGTAGGAAGTCCCAGGACGTGGGGTGTCAGGGCGGCCAAAAAGTAGACAAGCACGTGGGTCTGTCAGATACATAAGCTATCCAATCCTTGCCATAAGCTACATGGGATTAGGACCAAGAATCCGCATTCAGGTCCATTTGACGAATAGTGAAGCTCCTAGTGGAGTTCATTTGCGTCCGAGTTTACAAATCTTAGTCTTAGCTACGCGACTCTAGCG",7)
#print " ".join(str(item) for item in frequencyArray)


