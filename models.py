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
        # create font size stats
        self.docWordCount = self.getDocWordCount(self.pages)
        self.docLineCount = self.getDocLineCount(self.pages)
        #self.pageCount =
        docTexts = []
        for page in self.pages:
            docTexts += page["pageTexts"]
        self.docFontSizeStats = vars(FontSizeStats(docTexts, self.docWordCount))

    def createPages(self, pdf):
        pages = []
        
        for i, pageItem in enumerate(pdf):
            #print(json.dumps(pageItem))
            page = vars(Page(pageItem, i))
            pages.append(page)
        
        return pages
    
    def getDocWordCount(self, pages):
        docWordCount = 0
        for page in pages:
            docWordCount += page["pageWordCount"]
        return docWordCount
    
    def getDocLineCount(self, pages):
        docLineCount = 0
        for page in pages:
            docLineCount += page["pageLineCount"]
        return docLineCount

class Page:

    def __init__(self, textItems, pageNumber):
        self.pageNumber = pageNumber
        self.pageTexts = self.createPageTexts(textItems)
        self.pageWordCount = self.getPageWordCount(self.pageTexts)
        self.pageLineCount = self.getPageLineCount(self.pageTexts)
        self.pageFontSizeStats = vars(FontSizeStats(self.pageTexts, self.pageWordCount))

    def createPageTexts(self, textItems):
        texts = []
        
        for item in textItems:
                #print(json.dumps(item))
                text = vars(Text(item["str"], item["size"]))
                texts.append(text)
        
        return texts
    
    def getPageWordCount(self, texts):
        wordCount = 0
        for text in texts:
            wordCount += text["wordCount"]
        return wordCount

    def getPageLineCount(self, pageTexts):
        return len(pageTexts)

class Text:

    def __init__(self, str, fontSize):
        self.str = str
        self.wordCount = self.getWordCount(str)
        self.fontSize = fontSize

    def getWordCount(self, str):
        words = str.split()
        return len(words)


class FontSize:
    def __init__(self, size, count, mode, totalCount):
        self.size = size
        self.count = count
        self.frequency = self.getFrequency(count, totalCount)
        self.deviationFromMode = self.getDeviationFromMode(mode)
    
    def getFrequency(self, count, totalCount):
        return float(count)/totalCount
    
    def getDeviationFromMode(self, mode):
        return self.size - mode

class FontSizeStats:
    def __init__(self, texts, totalWordCount):
        # get all font sizes
        fontSizes = {}
        for item in texts:
            size = item["fontSize"]
            if size in fontSizes:
                fontSizes[size] += item["wordCount"]
            else:
                fontSizes[size] = item["wordCount"]
        
        self.fontSizes = fontSizes

        # get mode, largest, and smallest font size
        self.modeFontSize = max(fontSizes, key=lambda key: fontSizes[key])
        self.maxFontSize = max(k for k, v in fontSizes.iteritems())
        self.minFontSize = min(k for k, v in fontSizes.iteritems())

        for fontSize, count in self.fontSizes.items():
            self.fontSizes[fontSize] = vars(FontSize(fontSize, count, self.modeFontSize, totalWordCount))




