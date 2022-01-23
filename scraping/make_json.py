import json
import os

outp = open("idNums.txt", "w")

dirname = "clean_html"
for filename in os.listdir(dirname):
    fname = os.path.join(dirname, filename)
    if os.path.isfile(fname):
        f = open(fname, "r")
        plaintext = f.read()

        alllines = plaintext.splitlines()
        outp.write((alllines[0]) + "\n") 
