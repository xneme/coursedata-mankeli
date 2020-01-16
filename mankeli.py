from flask import Flask, escape, request, jsonify
import csv
import os
from magic import get_grades

app = Flask(__name__)


@app.route('/grades', methods=['POST'])
def grades():
    if (request.headers.get('Authorization') != os.environ.get('TOKEN')):
        return jsonify({'error': 'Invalid token!'}), 403
    grades = request.json
    return jsonify(get_grades(grades))


@app.route('/postgrades', methods=['POST'])
def postgrades():
    grades = request.json
    return jsonify(get_grades(grades))


@app.route('/getgrades', methods=['GET'])
def getgrades():
    grades = request.json
    return jsonify(get_grades({"Tietorakenteet ja algoritmit": 5,
                               "Ohjelmoinnin perusteet": 5,
                               "Design and Analysis of Algorithms": 5}))


@app.route('/ping')
def pong():
    return "pong!"


@app.route('/sample')
def sample():
    with open('data/sample.csv', 'r') as file:
        reader = csv.reader(file, delimiter=';')
        return jsonify(list(reader))
