#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Aplikace na hromadnou změnu velikosti fotek s možností přidání vodoznaku.
'''

import sys, os, shutil, datetime
from PySide import QtGui, QtCore
from mainUI import mainUI
from PIL import Image, ImageDraw, ImageFont, ImageEnhance

__author__ = 'Miroslav Suchánek'

class myUI(mainUI):

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
                    self.lblPocet.setText(self.transGUI('lblPocet')+"%s" % self.dbResize[2])
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
                    self.setItemToList(self.transGUI('copyLog_0')+' %s' % self.dbSource[2], QtCore.Qt.blue)

    # Funkce stisknutí tlačítka /Start/ pro spuštění procesu úpravy.
    def resizeImg(self):
        self.progress.setMaximum(int(self.dbResize[2]))
        self.btnStart.setEnabled(False)
        self.grpSlozka.setEnabled(False)
        self.grpUprava.setEnabled(False)
        self.grpWater.setEnabled(False)
        self.setThread = 'resize'

        self.res_allFiles = self.dbResize[1]
        self. res_nHeight = self.spnVyska.value()
        self.res_quality = self.spnKvalita.value()
        self.res_prefix = self.edtPrefix.text()+'_'
        self.res_nDirPath = os.path.join(self.dbResize[0], self.res_prefix)
        self.res_addW = self.grpWater.isChecked()
        self.res_textW = self.edtWater.text()

        if not os.path.exists(self.res_nDirPath):
            os.mkdir(self.res_nDirPath)

        rThread = ResizeTH()
        rThread.run()

    def setItemToList(self, text, color):
        item = QtGui.QListWidgetItem(text)
        item.setForeground(QtGui.QBrush(color))
        self.lstLog.insertItem(0, item)
        self.lstLog.repaint()

    # Funkce vyvolání info dialogu.
    def getInfo(self, title, text):
        ok = QtGui.QMessageBox.information(MainWindow, title, text)

    # Funkce pro informaci o dokončení procesu úpravy/přenosu.
    def threadFinished(self):
        if self.setThread == 'resize':
            if int(self.dbResize[2]) == self.progress.value():
                if self.grpWater.isChecked():
                    os.remove(self.tmp)
                self.defaultStatus()
                self.getInfo(self.transGUI('finishTitle_1'), self.transGUI('finishInfo_1'))
        elif self.setThread == 'copy':
            if int(self.dbSource[2]) == self.progPrenos.value():
                self.setItemToList(self.transGUI('copyLog_2'), QtCore.Qt.black)
                self.defaultStatus()
                if self.error:
                    self.getInfo(self.transGUI('finishTitle_2'), self.transGUI('finishInfo_3'))
                else:
                    self.getInfo(self.transGUI('finishTitle_1'), self.transGUI('finishInfo_2'))

    # Funkce překreslení (aktualizace) progresbaru.
    def progresUpdate(self):
        if self.setThread == 'resize':
            position = self.progress.value()
            self.progress.setValue(position + 1)
        elif self.setThread == 'copy':
            position = self.progPrenos.value()
            self.progPrenos.setValue(position + 1)

    # Funkce nastavení výchozích hodnot aplikace po ukončení procesu úpravy.
    def defaultStatus(self):
        if self.setThread == 'resize':
            self.grpSlozka.setEnabled(True)
            self.edtSlozka.clear()
            self.lblPocet.setText(self.transGUI('lblPocet'))
            self.spnVyska.setValue(600)
            self.spnKvalita.setValue(85)
            self.edtPrefix.setText('edited')
            self.grpUprava.setEnabled(False)
            self.edtWater.setText(self.transGUI('edtWater'))
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

    def addWatermark(self, in_file, out_file, text, quality, angle=23, opacity=0.25):

        FONT = os.path.join(self.myPath, 'inc', 'DVS-Bold.ttf')

        img = Image.open(in_file).convert('RGB')
        watermark = Image.new('RGBA', img.size, (0,0,0,0))
        size = 2
        n_font = ImageFont.truetype(FONT, size)
        n_width, n_height = n_font.getsize(text)

        while n_width+n_height < watermark.size[0]:
            size += 2
            n_font = ImageFont.truetype(FONT, size)
            n_width, n_height = n_font.getsize(text)

        draw = ImageDraw.Draw(watermark, 'RGBA')
        draw.text(((watermark.size[0] - n_width) / 2,
              (watermark.size[1] - n_height) / 2),
              text, font=n_font)

        watermark = watermark.rotate(angle, Image.BICUBIC)
        alpha = watermark.split()[3]
        alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
        watermark.putalpha(alpha)
        Image.composite(watermark, img, watermark).save(out_file, 'jpeg', quality=quality)

        # Funkce stisknutí tlačítka /Start/ pro spuštění přenosu souborů.

    def copyImg(self):
        self.progPrenos.setMaximum(int(self.dbSource[2]))
        self.btnPrenos.setEnabled(False)
        self.grpZdroj.setEnabled(False)
        self.grpCil.setEnabled(False)
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

class ResizeTH(QtCore.QThread):
    def __init__(self, parent=None):
        super(ResizeTH, self).__init__(parent)
        self.ui = myGui

    def run(self):
       for resizeFile in self.ui.res_allFiles:
            infile = os.path.join(self.ui.dbResize[0], resizeFile)
            outfile = os.path.join(self.ui.res_nDirPath, self.ui.res_prefix+resizeFile)
            self.ui.tmp = os.path.join(self.ui.res_nDirPath, '.tmpImg')
            rFile = Image.open(infile)
            width, height = rFile.size
            pomer = round(height / self.ui.res_nHeight, 2)
            nWidth = round(width / pomer)
            if self.ui.res_addW:
                rFile.resize((nWidth, self.ui.res_nHeight), Image.ANTIALIAS).save(self.ui.tmp, 'jpeg', quality=self.ui.res_quality)
                self.ui.addWatermark(self.ui.tmp, outfile, self.ui.res_textW, self.ui.res_quality)
            else:
                rFile.resize((nWidth, self.ui.res_nHeight), Image.ANTIALIAS).save(outfile, 'jpeg', quality=self.ui.res_quality)
            self.ui.progresUpdate()

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
            self.ui.setItemToList(self.ui.transGUI('copyLog_3')+' %s' % e, QtCore.Qt.red)
            self.ui.error = True
        # pokud zdroj nebo cíl neexistuje
        except IOError as e:
            self.ui.lstLog.takeItem(0)
            self.ui.setItemToList(self.ui.transGUI('copyLog_3')+' -- %s -- %s' % (self.file, e.strerror), QtCore.Qt.red)
            self.ui.error = True
        finally:
            self.ui.progresUpdate()

# Výchozí funkce spuštění aplikace

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    myGui = myUI()
    myGui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())