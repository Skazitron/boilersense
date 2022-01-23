from flask import Flask
from flask_cors import CORS
import json
from flask import jsonify


app = Flask(__name__)
CORS(app)
jsonfile = open("idData.json")
json = json.load(jsonfile)

@app.route("/", methods=['GET'])
def startup():
    return jsonify(json)
