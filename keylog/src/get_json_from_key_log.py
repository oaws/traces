import json
import datetime
inputFile = open("/Users/joemanley/.traces/key.log")

keylogdata = {}
for line in inputFile:
    processedLine = eval(line)
    rawDateTimeInMilliSec = datetime.datetime.fromtimestamp(processedLine["time"])
    extractedDate = rawDateTimeInMilliSec.date().__str__()
    if extractedDate not in keylogdata:
        keylogdata[extractedDate] = 0

    keylogdata[extractedDate] += 1
jsonString = json.dumps(keylogdata)
outputFile = open("/Users/joemanley/workspace/traces_220/keylog/data/data.json", "w")
outputFile.write("var keylogData = " + jsonString)
outputFile.close()