import json


class Catalog:
    def __init__(self, filename) -> None:
        self.jsonfile = json.load(open(filename, "r"))
    def getInfo(self, courseNum):
        return (self.jsonfile)[courseNum]
