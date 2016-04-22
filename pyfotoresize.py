#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Application for mass resizing photos with the possibility of adding watermark.
Aplikace na hromadnou změnu velikosti fotek s možností přidání vodoznaku.
'''

import sys, os, shutil, datetime
from PySide import QtGui, QtCore
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
from fotoResizeGUI import fotoResizeGUI

__author__ = 'Miroslav Suchánek'

class myUI(fotoResizeGUI):

    # Funkce pro zvolení požadované složky
    def openDir(self, ident, text):
        dirname = QtGui.QFileDialog.getExistingDirectory(None, text, os.getenv('HOME'))
        if dirname:
            images = []
            for file in os.listdir(dirname):
                if file.lower().endswith(".jpg") or file.lower().endswith(".jpeg"):
                    images.append(file)
            if ident == 'cil':
                    self.dbTarget = []
                    self.dbTarget.insert(0, dirname)

                    self.edtCil.setText(dirname)
                    self.grpPrenos.setEnabled(True)
                    self.btnPrenos.setEnabled(True)
            if len(images) > 0:
                if ident == 'zmena':
                    self.dbResize = []
                    self.dbResize.insert(0, dirname)
                    self.dbResize.insert(1, images)
                    self.dbResize.insert(2, str(len(images)))

                    self.edtSlozka.setText(dirname)
                    self.lblPocet.setText(self.translator.translate('lblPocet')+"%s" % self.dbResize[2])
                    self.grpUprava.setEnabled(True)
                    self.grpWater.setEnabled(True)
                    self.grpStart.setEnabled(True)
                    self.btnStart.setEnabled(True)

                elif ident == 'zdroj':
                    self.dbSource = []
                    self.dbSource.insert(0, dirname)
                    self.dbSource.insert(1, images)
                    self.dbSource.insert(2, str(len(images)))

                    self.edtZdroj.setText(dirname)
                    self.grpCil.setEnabled(True)
                    self.lstLog.clear()
                    self.setItemToList(self.translator.translate('copyLog_0')+' %s' % self.dbSource[2], QtCore.Qt.blue)

    # Funkce stisknutí tlačítka /Start/ pro spuštění procesu úpravy.
    def resizeImg(self):
        self.progress.setMaximum(int(self.dbResize[2]))
        self.btnStart.setEnabled(False)
        self.grpSlozka.setEnabled(False)
        self.grpUprava.setEnabled(False)
        self.grpWater.setEnabled(False)
        self.btnExit.setEnabled(False)
        self.setThread = 'resize'

        self.res_nHeight = self.spnVyska.value()
        self.res_quality = self.spnKvalita.value()
        self.res_prefix = self.edtPrefix.text()
        self.res_addW = self.grpWater.isChecked()
        self.res_textW = self.edtWater.text()

        edt = EditImage(self.dbResize)
        edt.resizeFoto(self.res_nHeight, self.res_prefix, self.res_quality, self.res_addW, self.res_textW)

    # Funkce stisknutí tlačítka /Start/ pro spuštění kopírování souborů.
    def copyImg(self):
        self.progPrenos.setMaximum(int(self.dbSource[2]))
        self.btnPrenos.setEnabled(False)
        self.grpZdroj.setEnabled(False)
        self.grpCil.setEnabled(False)
        self.btnExit.setEnabled(False)
        self.setThread = 'copy'

        sourcePath = self.dbSource[0]
        targetPath = self.dbTarget[0]
        copyFiles = self.dbSource[1]

        if os.path.exists(sourcePath) and os.path.isdir(sourcePath):
            if os.path.exists(targetPath) and os.path.isdir(targetPath):
                self.setItemToList(self.transGUI('copyLog_4')+' %s' % sourcePath, QtCore.Qt.black)
                self.setItemToList(self.transGUI('copyLog_5')+' %s' % targetPath, QtCore.Qt.black)
                self.setItemToList(self.transGUI('copyLog_1'), QtCore.Qt.black)
                c = 0
                self.error = False
                for cFile in copyFiles:
                    c += 1
                    pocitadlo = '{0:0>3}'.format(c)
                    datum = datetime.datetime.now()
                    newFilename = '%s%s%s%s' % ('P', datum.strftime('%d%m%H%M-'), pocitadlo, '.jpg')
                    self.setItemToList('%i/%s..........%s --> %s' % (c, self.dbSource[2], cFile, newFilename), QtCore.Qt.darkGreen)
                    cThread = CopyTH(os.path.join(sourcePath, cFile), os.path.join(targetPath, newFilename), cFile)
                    cThread.run()

    # Funkce vytvoření a přidání informace do logu
    def setItemToList(self, text, color):
        item = QtGui.QListWidgetItem(text)
        item.setForeground(QtGui.QBrush(color))
        self.lstLog.insertItem(0, item)
        self.lstLog.repaint()

    # Funkce vyvolání info dialogu.
    def getInfo(self, title, text):
        ok = QtGui.QMessageBox.information(MainWindow, title, text)

    # Funkce překreslení (aktualizace) progresbaru.
    def progresUpdate(self):
        if self.setThread == 'resize':
            position = self.progress.value()
            self.progress.setValue(position + 1)
        elif self.setThread == 'copy':
            position = self.progPrenos.value()
            self.progPrenos.setValue(position + 1)

    # Funkce pro informaci o dokončení procesu úpravy/přenosu.
    def threadFinished(self):
        if self.setThread == 'resize':
            if int(self.dbResize[2]) == self.progress.value():
                if self.grpWater.isChecked():
                    os.remove(self.tmp)
                self.defaultStatus()
                self.getInfo(self.translator.translate('finishTitle_1'), self.translator.translate('finishInfo_1'))
        elif self.setThread == 'copy':
            if int(self.dbSource[2]) == self.progPrenos.value():
                self.setItemToList(self.translator.translate('copyLog_2'), QtCore.Qt.black)
                self.defaultStatus()
                if self.error:
                    self.getInfo(self.translator.translate('finishTitle_2'), self.translator.translate('finishInfo_3'))
                else:
                    self.getInfo(self.translator.translate('finishTitle_1'), self.translator.translate('finishInfo_2'))

    # Funkce nastavení výchozích hodnot aplikace po ukončení procesu úpravy.
    def defaultStatus(self):
        self.btnExit.setEnabled(True)
        if self.setThread == 'resize':
            self.grpSlozka.setEnabled(True)
            self.edtSlozka.clear()
            self.lblPocet.setText(self.translator.translate('lblPocet'))
            self.spnVyska.setValue(600)
            self.spnKvalita.setValue(85)
            self.edtPrefix.setText('edited')
            self.grpUprava.setEnabled(False)
            self.edtWater.setText(self.translator.translate('edtWater'))
            self.grpWater.setChecked(False)
            self.grpWater.setEnabled(False)
            self.progress.setValue(0)
            self.grpStart.setEnabled(False)
        elif self.setThread == 'copy':
            self.grpZdroj.setEnabled(True)
            self.edtZdroj.clear()
            self.grpCil.setEnabled(False)
            self.edtCil.clear()
            self.grpPrenos.setEnabled(False)
            self.progPrenos.setValue(0)

class EditImage:

    dataFiles = None # 1 = dirPath, 2 = list_of_Files, 3 = number_of_files

    def __init__(self, data_of_Files):
        self.dataFiles = data_of_Files

    def getNewSize(self, origSize, newHeight):
        origWidth, origHeight = origSize
        ratio = round(origHeight / newHeight, 2)
        newWidth = round(origWidth / ratio)
        newSize = [newWidth, newHeight]
        return newSize

    def createNewFoto(self, newPathsDB, newCreateDB):
        # newPathsDB = [newDirPath, newFileName, tmpFileName]
        # newCreateDB = [newHeight, savePrefix, qualily_img, watermark, wtmText]
        for resizeFile in self.dataFiles[1]:
            inFile = os.path.join(self.dataFiles[0], resizeFile)
            outFile = newPathsDB[1] + resizeFile
            origFoto = Image.open(inFile)
            if newCreateDB[3]:
                origFoto.resize(self.getNewSize(origFoto.size, newCreateDB[0]), Image.ANTIALIAS).save(newPathsDB[2], 'jpeg', quality=newCreateDB[2])
                fontPath = os.path.join(sys.path[0], 'inc', 'wtm_font.ttf')
                self.addWatermark(newPathsDB[2], outFile, newCreateDB[4], fontPath, newCreateDB[2])
            else:
                origFoto.resize(self.getNewSize(origFoto.size, newCreateDB[0]), Image.ANTIALIAS).save(outFile, 'jpeg', quality=newCreateDB[2])
            myGui.progresUpdate()

    def resizeFoto(self, newHeight, savePrefix='resized', qualily_img=85, watermark=False, wtmText=None):

        newDirPath = os.path.join(self.dataFiles[0], savePrefix)
        newFileName = os.path.join(newDirPath, savePrefix+'_')
        tmpFileName = os.path.join(newDirPath, '.tmp_image')
        myUI.tmp = tmpFileName

        pathsData = [newDirPath, newFileName, tmpFileName]
        createData = [newHeight, savePrefix, qualily_img, watermark, wtmText]

        if not os.path.exists(newDirPath):
            os.mkdir(newDirPath)

        self.createNewFoto(pathsData, createData)

    def getPosition(self, imgSize, wtmSize, idp):
        # 0 = fullscreen, 1 = left-top, 2 = left-bottom, 3 = right-top, 4 = right-bottom
        left_pos, top_pos = [0, 0]
        if idp == 0:
            left_pos = (imgSize[0] - wtmSize[0]) / 2
            top_pos = (imgSize[1] - wtmSize[1]) / 2
        elif idp == 1:
            left_pos = wtmSize[0] / 4
            top_pos = wtmSize[0] / 4
        elif idp == 2:
            left_pos = wtmSize[0] / 4
            top_pos = imgSize[1] - (wtmSize[1] + (wtmSize[0] / 4))
        elif idp == 3:
            left_pos = imgSize[0] - (wtmSize[0] + (wtmSize[0] / 4))
            top_pos = wtmSize[0] / 4
        elif idp == 4:
            left_pos = imgSize[0] - (wtmSize[0] + (wtmSize[0] / 4))
            top_pos = imgSize[1] - (wtmSize[1] + (wtmSize[0] / 4))
        position = [left_pos, top_pos]
        return position

    def addWatermark(self, inFile, outFile, textWatermark, font_file, qualityImg, wtm_type='fullscreen', angle=26, opacity=0.25):

        original_img = Image.open(inFile).convert('RGB')
        empty_img = Image.new('RGBA', original_img.size, (0,0,0,0))

        font_size = 2
        wtm_text = ImageFont.truetype(font_file, font_size)
        wtm_width, wtm_height = wtm_text.getsize(textWatermark)

        if wtm_type == 'fullscreen':
            idp = 0
            while wtm_width + wtm_height < empty_img.size[0]:
                font_size += 2
                wtm_text = ImageFont.truetype(font_file, font_size)
                wtm_width, wtm_height = wtm_text.getsize(textWatermark)
        elif wtm_type == 'stamp':
            idp = 4
            while wtm_width + wtm_height < empty_img.size[0] / 5:
                font_size += 2
                wtm_text = ImageFont.truetype(font_file, font_size)
                wtm_width, wtm_height = wtm_text.getsize(textWatermark)

        wtm_size = [wtm_width, wtm_height]

        wtm_draw = ImageDraw.Draw(empty_img, 'RGBA')
        wtm_draw.text(self.getPosition(empty_img.size, wtm_size, idp), textWatermark, font=wtm_text)

        empty_img = empty_img.rotate(angle, Image.BICUBIC)
        alpha = empty_img.split()[3]
        alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
        empty_img.putalpha(alpha)
        Image.composite(empty_img, original_img, empty_img).save(outFile, 'jpeg', quality=qualityImg)

class CopyTH(QtCore.QThread):
    def __init__(self, infile, outfile, file, parent=None):
        super(CopyTH, self).__init__(parent)
        self.ui = myGui
        self.infile = infile
        self.outfile = outfile
        self.file = file

    def run(self):
        try:
            shutil.copy(self.infile, self.outfile)
        # je-li zdroj a cíl stejný
        except shutil.Error as e:
            self.ui.lstLog.takeItem(0)
            self.ui.setItemToList(self.ui.translator.translate('copyLog_3')+' %s' % e, QtCore.Qt.red)
            self.ui.error = True
        # pokud zdroj nebo cíl neexistuje
        except IOError as e:
            self.ui.lstLog.takeItem(0)
            self.ui.setItemToList(self.ui.translator.translate('copyLog_3')+' -- %s -- %s' % (self.file, e.strerror), QtCore.Qt.red)
            self.ui.error = True
        finally:
            self.ui.progresUpdate()

# Výchozí funkce spuštění aplikace

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    myGui = myUI()
    myGui.createGUI(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())