#!/usr/bin/env python3

from __future__ import print_function
from flask import Flask, jsonify, render_template, request
from models import Document, Page, Text
import json
import sys
import time
from scipy import stats

application = Flask(__name__, static_folder='static')

def normalize(val, min, max):
    return (val-min)/(max-min)

def processTexts(pdf):
    # create a list of font sizes
    # create a list of spacings
    for page in pdf:
        fontSizes = []
        spacings = []
        for text in page:
            fontSizes.append(text["fontSize"])
            if text["spacing"] > 0:
                spacings.append(text["spacing"])
        fontSizes.sort()
        spacings.sort()
        
        # get max and min for font sizes and spacings
        maxFontSize = fontSizes[len(fontSizes)-1]
        minFontSize = fontSizes[0]

        maxSpacing = spacings[len(spacings)-1]
        minSpacing = spacings[0]

        ratios = []
        
        for text in page:
            text["fontSize"] = normalize(text["fontSize"], minFontSize, maxFontSize)
            text["spacing"] = normalize(text["spacing"], minSpacing, maxSpacing)
            text["ratio"] = 0
            if text["spacing"] > 0:
                text["ratio"] = text["fontSize"]/text["spacing"]
            ratios.append(text["ratio"])

        # sort ratios and get min and max
        ratios.sort()
        minRatio = ratios[0]
        maxRatio = ratios[len(ratios)-1]

        for text in page:
            text["ratio"] = normalize(text["ratio"], minRatio, maxRatio)


@application.route('/')
def index():
    return render_template('index.html')

@application.route('/compute-text-stats/', methods = ['GET','POST'])
def computeTextStats():
    start = time.time()
    pdf = request.json
    processTexts(pdf)
    end = time.time()
    response = {}
    response["pdf"] = pdf
    response["time"] = round(end- start, 4)
    return jsonify(response)
    
if __name__ == "__main__":
    application.run(debug=True)