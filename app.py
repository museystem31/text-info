#!/usr/bin/env python3

from __future__ import print_function
from flask import Flask, jsonify, render_template, request
import json
import sys

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compute-text-stats/', methods = ['GET','POST'])
def computeTextStats():
    data= request.json
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)