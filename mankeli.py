from flask import Flask, escape, request, jsonify
import csv
import os

app = Flask(__name__)



@app.route('/grades/<studentnumber>')
def hello(studentnumber):
  if (request.headers.get('Authorization') != os.environ.get('TOKEN')):
    return jsonify({ 'error': 'Invalid token!'}), 403

  grades = {
    "014": {
      0: {"course": "TIRA", "grade": 5, "generated": True},
      1: {"course": "TITO", "grade": 4, "generated": False},
      2: {"course": "OHPE", "grade": 3, "generated": False}
    },
    "015": {
      0: {"course": "TIRA", "grade": 1, "generated": True},
      1: {"course": "TITO", "grade": 2, "generated": False},
      2: {"course": "OHPE", "grade": 2, "generated": False}
    }
  }

  return jsonify(grades[studentnumber])

@app.route('/ping')
def pong():
  return "pong!"

@app.route('/sample')
def sample():
  with open('data/sample.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    return jsonify(list(reader))
