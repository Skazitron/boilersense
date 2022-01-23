from flask import Flask
import json
from flask import jsonify

app = Flask(__name__)
jsonfile = open("idData.json")
json = json.load(jsonfile)

@app.route("/", methods=['GET'])
def startup():
    return jsonify(json)
