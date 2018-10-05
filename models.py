#!/usr/bin/env python3
import json
import codecs
import operator
from collections import Counter
'''
Document stats: word count, line count, font sizes stats, pages stats
#Page stats: word count, line count, lines stats, font sizes stats
Font sizes stats: font sizes, mode font size, max font size, min font size
Font size stats: size, count, frequency in %, deviation from mode
#Line stats: string, string length, word count, font size, font family, distances to margins
'''
class Document:

    def __init__(self, pdf):
        # create pages
        self.pages = self.createPages(pdf)

    def createPages(self, pdf):
        pages = []
        
        for i, pageItem in enumerate(pdf):
            page = vars(Page(pageItem, i))
            pages.append(page)
        
        return pages

class Page:

    def __init__(self, textItems, pageNumber):
        self.pageNumber = pageNumber
        self.pageTexts = self.createPageTexts(textItems)

    def createPageTexts(self, textItems):
        texts = TextProcesser.processTexts(textItems)
        return vars(texts)

class Text:

    def __init__(self, str, fontSize, length, x, y, spacing, ratio):
        self.str = str
        self.wordCount = self.getWordCount(str)
        self.fontSize = fontSize
        self.length = length
        self.x = x
        self.y = y
        self.spacing = spacing
        self.ratio = ratio

    def getWordCount(self, str):
        words = str.split()
        return len(words)

class TextProcesser:
    @staticmethod
    def processTexts(textItems):
        # get all the font sizes, max and min
        fontSizes = []
        for item in textItems:
            fontSizes.append(item["fontSize"])
        
        # get all the spacing max and min
        spacings = []
        
        pass





