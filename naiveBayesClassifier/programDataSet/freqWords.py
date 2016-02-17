__author__ = 'Srinivas Avireddy'

def freqWords(string,k):
    freqWords = {}
    maxCount = 0
    for i in xrange(0,len(string)-k+1):
        currentStr = string[i:i+k]
        currentCount = 0
        if currentStr not in freqWords:
            currentCount = 1
            freqWords[currentStr] = 1
        else:
            freqWords[currentStr] += 1
            currentCount = freqWords[currentStr]

        if currentCount > maxCount:
            maxCount = currentCount

    freqWordString = ""
    for str in freqWords:
        if freqWords[str] == maxCount:
            freqWordString += str + " "
    print freqWordString

freqWords("TTCGCCTGTGCATAGGGATTTCGCCTGTGACATACCCAACATACCCAATGATTGTGTTCGCCTGTGCATAGGGATACATACCCACATAGGGATCTGGGGGATTCGCCTGTGATGATTGTGCTGGGGGATTCGCCTGTGATGATTGTGACATACCCACTGGGGGAACATACCCAATGATTGTGCTGGGGGAACATACCCATTCGCCTGTGCTGGGGGATTCGCCTGTGCTGGGGGACTGGGGGAATGATTGTGACATACCCAACATACCCATTCGCCTGTGTTCGCCTGTGCATAGGGATACATACCCAACATACCCAATGATTGTGTTCGCCTGTGCATAGGGATCATAGGGATATGATTGTGCTGGGGGAACATACCCACTGGGGGATTCGCCTGTGTTCGCCTGTGACATACCCATTCGCCTGTGTTCGCCTGTGCATAGGGATATGATTGTGCTGGGGGAATGATTGTGACATACCCAATGATTGTGACATACCCAATGATTGTGATGATTGTGCTGGGGGATTCGCCTGTGCTGGGGGAATGATTGTGACATACCCACATAGGGATCTGGGGGATTCGCCTGTGCTGGGGGATTCGCCTGTGCTGGGGGATTCGCCTGTGCATAGGGATACATACCCAATGATTGTGCTGGGGGACTGGGGGAATGATTGTGTTCGCCTGTGTTCGCCTGTGATGATTGTGTTCGCCTGTGATGATTGTGTTCGCCTGTGACATACCCAACATACCCACTGGGGGATTCGCCTGTGTTCGCCTGTGACATACCCAACATACCCATTCGCCTGTGTTCGCCTGTGTTCGCCTGTGACATACCCACTGGGGGAATGATTGTGCTGGGGGACATAGGGATCTGGGGGAATGATTGTGTTCGCCTGTGCATAGGGATACATACCCAACATACCCACTGGGGGACATAGGGATCATAGGGATCTGGGGGAATGATTGTGACATACCCACATAGGGAT",11)