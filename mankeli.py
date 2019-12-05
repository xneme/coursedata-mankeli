from flask import Flask, escape, request, jsonify
import csv
import os
from magic import get_grades

app = Flask(__name__)

grades = get_grades()

@app.route('/grades/<studentnumber>')
def hello(studentnumber):
  if (request.headers.get('Authorization') != os.environ.get('TOKEN')):
    return jsonify({ 'error': 'Invalid token!'}), 403

  return jsonify(grades[studentnumber])

@app.route('/ping')
def pong():
  return "pong!"

@app.route('/sample')
def sample():
  with open('data/sample.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    return jsonify(list(reader))
