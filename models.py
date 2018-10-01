#!/usr/bin/env python3
import json
'''
Document stats: word count, line count, font sizes stats, pages stats
#Page stats: word count, line count, lines stats, font sizes stats
Font sizes stats: font sizes, mode font size, max font size, min font size
Font size stats: size, count, frequency in %, deviation from mode
#Line stats: string, string length, word count, font size, font family, distances to margins
'''

class Text:

    def __init__(self, str, fontSize):
        self.str = str
        self.wordCount = self.getWordCount(str)
        self.fontSize = fontSize

    def getWordCount(self, str):
        words = str.split(" ")
        return len(words)

class Page:

    def __init__(self, texts, pageNumber):
        self.pageNumber = pageNumber

    def createTexts(self, textItems):
        texts = []
        
        for item in textItems:
            text = Text(item["str"], item["size"])
            texts.append(text)
        
        return texts

class Document:

    def __init__(self, pdf):
        # create pages
        self.pages = self.createPages(pdf)

    def createPages(self, pdf):
        pages = []
        
        for i, item in enumerate(pdf):
            page = Page(item, i)
            pages.append(page)
        
        return pages

"""
class Font:
    def __init__(self, family, size, count, frequency, deviationFromMode):
        self.family = family
        self.size = size
        self.count = count
        self.frequency = frequency
        self.deviationFromMode = deviationFromMode
"""




