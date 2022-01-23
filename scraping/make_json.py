import json
import os
from pydoc import plain
import re
import time

extract_credit = re.compile("([0-9])+\.([0-9])+")
prefix_snipper = re.compile("([A-z]|\ )+:")
rcn = re.compile("Credit Hours: ([0-9])+\.([0-9])+\.")


mainObject = {}
os_output = open("course_dump.json", "w")

dirname = "clean_html"
for filename in os.listdir(dirname):
    fname = os.path.join(dirname, filename)
    if os.path.isfile(fname):
        f = open(fname, "r")
        plaintext = f.read()
        alllines = plaintext.splitlines()
        spltline = alllines[0].split(" - ")
        insidedict = {}
        insidedict["courseName"] = spltline[1].replace('\n', '')
        
        i = 0
        while i < len(alllines):
            if alllines[i].find("Credit Hours: ") != -1:
                credisent = extract_credit.search(alllines[i])
                if credisent == None:
                    insidedict["credits"] = -1
                else:
                    cred = credisent.group(0)
                    insidedict["credits"] = float(cred)
                alllines[i] = re.sub(rcn, '', alllines[i])
                curstring = ""
                while alllines[i]:
                    curstring += alllines[i]
                    i+=1
                insidedict["description"] = curstring.strip()
            if alllines[i].find("Schedule Types:") != -1:
                alllines[i] = re.sub(prefix_snipper, '', alllines[i])
                categ = alllines[i].split(",")
                for j in range(len(categ)):
                    categ[j] = categ[j].strip()
                insidedict["schedule"] = categ
            if alllines[i].find("Offered By:") != -1:
                alllines[i] = re.sub(prefix_snipper, '', alllines[i])
                insidedict["offeredby"] = alllines[i].strip()
            if alllines[i].find("Department:") != -1:
                alllines[i] = re.sub(prefix_snipper, '', alllines[i])
                insidedict["department"] = alllines[i].strip()
            i+=1
        mainObject[spltline[0]] = insidedict


json.dump(mainObject, os_output)
