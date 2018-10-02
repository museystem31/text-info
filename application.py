#!/usr/bin/env python3

from __future__ import print_function
from flask import Flask, jsonify, render_template, request
from models import Document, Page, Text
import json
import sys

application = Flask(__name__, static_folder='static')

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/compute-text-stats/', methods = ['GET','POST'])
def computeTextStats():
    pdf = request.json
    doc = Document(pdf)
    #response = {}
    return jsonify(vars(doc))

if __name__ == "__main__":
    application.run()