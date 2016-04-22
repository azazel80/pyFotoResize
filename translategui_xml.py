# -*- coding: utf-8 -*-

import xml.etree.ElementTree as etree

class translategui_xml:

    xmlFilePath = None
    xmlFile = None
    rootElement = None
    activeLangID = None
    allLangID = None
    allLangPict = None
    allLanguages = None

    def __init__(self, filePath):
        self.xmlFilePath = filePath
        self.xmlFile = etree.parse(self.xmlFilePath)
        self.activeLangID = self.getActiveLangID()
        self.setAllLanguages('.//lang')

    def setAllLanguages(self, elementName):
        self.allLanguages = self.xmlFile.findall(elementName)
        self.allLangID = []
        self.allLangPict = []
        for lang_id in self.allLanguages:
            self.allLangID.append((lang_id.get('id'),':icons/inc/vlajky/'+lang_id.get('id')+'.png'))

    def getActiveLangID(self):
        if not self.xmlFile == None:
            self.rootElement = self.xmlFile.getroot()
            return self.rootElement.get('active')

    def changeActiveLangID(self, newID):
        self.activeLangID = newID
        self.rootElement.set('active', newID)
        self.xmlFile.write(self.xmlFilePath, encoding='utf-8')

    def translate(self, componentName):
        for i, lang in enumerate(self.allLanguages):
            if self.allLangID[i][0] == self.activeLangID:
                for component in lang:
                    if component.tag == componentName:
                        return component.text