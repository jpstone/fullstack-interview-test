from flask import Flask 
from flask import jsonify 
import json

app = Flask(__name__)
db = json.load(open('db.json', 'r'));

# Delete/modify this code to create your API here
@app.route("/")
def default():
    return jsonify(db);
