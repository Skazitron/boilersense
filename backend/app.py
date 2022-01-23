from flask import Flask
from flask import request
import json
from flask import jsonify
from Catalog import Catalog
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

jsonfile = open("idData.json", "r")
jsonnames = json.load(jsonfile)

c = Catalog("course_dump.json")


@app.route("/", methods=['GET'])
def startup():
    return jsonify(jsonnames)

@app.route("/modaldata", methods=["GET"])
def modaldata():
    r = request.args.get('num')
    return jsonify(c.getInfo(r))
