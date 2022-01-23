import json

f = open("idNums.txt", "r")
out = open("idData.json", "w")

pythondict = [] 
count = 1 
for line in f:
    spltline = line.split(" - ")
    obj = {}
    obj["id"] = count
    obj["courseNumber"] = spltline[0]
    obj["courseName"] = spltline[1].replace('\n', '')
    count += 1
    pythondict.append(obj)


json.dump(pythondict, out)


##
## {0:[{key:value}, {}]}
##
