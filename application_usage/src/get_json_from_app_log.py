import json

inputFile = open("/Users/joemanley/.traces/app.log")
appData = {}
appData["data"] = {}
for line in inputFile:
    processedLine = eval(line)
    app = processedLine["app"]
    state = processedLine["type"]
    time = processedLine["time"]
    if "startTime" not in appData:
        appData["startTime"] = time
    appData["endTime"] = time
    if app not in appData["data"]:
        if state != "Active":
            continue
        else:
            appData["data"][app] = []
    if state == "Active":
        appData["data"][app].append({"startTime": time, "endTime": 0})
    if state in ["Close", "Inactive"]:
        appEntriesList = appData["data"][app]
        currentEntry = appEntriesList[len(appEntriesList) - 1]
        currentEntry["endTime"] = time
        currentEntry["duration"] = currentEntry["endTime"] - currentEntry["startTime"]

jsonString = json.dumps(appData)
outputFile = open("/Users/joemanley/workspace/traces_220/application_usage/data/data.json", "w")
outputFile.write("var appData = " + jsonString)
outputFile.close()