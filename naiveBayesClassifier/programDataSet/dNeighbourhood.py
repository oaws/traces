__author__ = 'Srinivas Avireddy'

def immediateNeighbors(string):
    neighbors = []
    for i in xrange(0,len(string)):
        for c in "ACGT":
            if string[i] != c:
                neighbor = string[0:i] + c + string[i+1:len(string)]
                neighbors.append(neighbor)
    return neighbors

def dNeighborHood(string,d):
    neighborhood = []
    neighborhood.append(string)
    for i in xrange(0,d):
        tempNeighborhood = []
        for s in neighborhood:
            immediateNeighbor = immediateNeighbors(s)
            tempNeighborhood.extend(immediateNeighbor)
        neighborhood.extend(tempNeighborhood)
        neighborhood = list(set(neighborhood))
    return neighborhood


def writeOutputToFile(output):
    f = open("dneighbors.txt","w")
    for item in output:
        f.write(item)
        f.write("\n")
    f.close()

#print writeOutputToFile(dNeighborHood("AATAGGCG",2))