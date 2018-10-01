#!/usr/bin/env python3
import json
import codecs
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
            #print(json.dumps(pageItem))
            page = vars(Page(pageItem, i))
            pages.append(page)
        
        return pages

class Page:

    def __init__(self, textItems, pageNumber):
        self.pageNumber = pageNumber
        self.texts = self.createTexts(textItems)
        #print(pageNumber)

    def createTexts(self, textItems):
        texts = []
        
        for item in textItems:
                #print(json.dumps(item))
                text = vars(Text(item["str"], item["size"]))
                texts.append(text)
        
        return texts

class Text:

    def __init__(self, str, fontSize):
        self.str = str
        self.wordCount = self.getWordCount(str)
        self.fontSize = fontSize

    def getWordCount(self, str):
        words = str.split()
        return len(words)

"""
class Font:
    def __init__(self, family, size, count, frequency, deviationFromMode):
        self.family = family
        self.size = size
        self.count = count
        self.frequency = frequency
        self.deviationFromMode = deviationFromMode
"""




