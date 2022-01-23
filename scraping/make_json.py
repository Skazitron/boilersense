import json
import os
import re

extract_credit = re.compile("([0-9])+\.([0-9])+")

print(extract_credit.match("How do yaa do boye. 3.00"))

rcn = re.compile("Credit Hours: ([0-9])+\.([0-9])+\.")


mainObject = {}


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
            if alllines[i].find("Credit Hours:") != -1:
                credsent = rcn.match(alllines[i])
                cred = extract_credit.match(alllines[i])
                alllines[i] = re.sub(rcn, '', alllines[i])
                curstring = ""
                while alllines[i]:
                    curstring += alllines[i]
                    i+=1
                insidedict["description"] = curstring.strip()
            i+=1
        mainObject[spltline[0]] = insidedict
        print(mainObject)
        break
