# -*- coding: utf-8 -*-

import sys, os, xml.etree.ElementTree as etree
from PySide import QtCore, QtGui

# Uživatelské prostředí aplikace
class mainUI(QtGui.QWidget):

    # Funkce inicialzace aplikace.
    def __init__(self):
        self.myPath = sys.path[0]
        self.transFilePath = os.path.join(self.myPath, 'inc', 'translate.xml')
        self.langXMLfile = etree.parse(self.transFilePath)
        if self.langXMLfile != '':
            self.rootElem = self.langXMLfile.getroot()
            self.langID = self.rootElem.get('active')

    # Funkce sestavení GUI aplikace (grafické uživatelské rozhraní).
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(492, 570)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")

        font = QtGui.QFont()
        font.setPointSize(10)
        logFont = QtGui.QFont()
        logFont.setPointSize(9)

        self.btnExit = QtGui.QPushButton(self.centralWidget)
        self.btnExit.setGeometry(QtCore.QRect(370, 480, 99, 27))
        self.btnExit.setObjectName("btnExit")
        self.btnExit.clicked.connect(QtGui.qApp.quit)

        self.lblCC = QtGui.QLabel(self.centralWidget)
        self.lblCC.setGeometry(QtCore.QRect(15, 478, 91, 31))
        self.lblCC.setOpenExternalLinks(True)
        self.lblCC.setObjectName("lblCC")

        self.lblPy = QtGui.QLabel(self.centralWidget)
        self.lblPy.setGeometry(QtCore.QRect(125, 478, 78, 31))
        self.lblPy.setOpenExternalLinks(True)
        self.lblPy.setObjectName("lblPy")

        self.lblGit = QtGui.QLabel(self.centralWidget)
        self.lblGit.setGeometry(QtCore.QRect(221, 478, 32, 32))
        self.lblGit.setOpenExternalLinks(True)
        self.lblGit.setObjectName("lblGit")

        self.tabWidget = QtGui.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(5, 5, 481, 461))
        self.tabWidget.setMouseTracking(True)
        self.tabWidget.setObjectName("tabWidget")

        # Tab úprava fotek
        self.tabResize = QtGui.QWidget()
        self.tabResize.setObjectName("tabResize")

        self.grpWater = QtGui.QGroupBox(self.tabResize)
        self.grpWater.setEnabled(False)
        self.grpWater.setGeometry(QtCore.QRect(3, 270, 471, 65))
        self.grpWater.setCheckable(True)
        self.grpWater.setChecked(False)
        self.grpWater.setObjectName("grpWater")

        self.layoutWidget = QtGui.QWidget(self.grpWater)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 451, 29))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.lblWater = QtGui.QLabel(self.layoutWidget)
        self.lblWater.setObjectName("lblWater")
        self.horizontalLayout_3.addWidget(self.lblWater)

        self.edtWater = QtGui.QLineEdit(self.layoutWidget)
        self.edtWater.setObjectName("edtWater")
        self.horizontalLayout_3.addWidget(self.edtWater)

        self.grpSlozka = QtGui.QGroupBox(self.tabResize)
        self.grpSlozka.setGeometry(QtCore.QRect(3, 17, 469, 117))
        self.grpSlozka.setObjectName("grpSlozka")

        self.lblSlozka = QtGui.QLabel(self.grpSlozka)
        self.lblSlozka.setGeometry(QtCore.QRect(10, 30, 201, 17))
        self.lblSlozka.setObjectName("lblSlozka")

        self.lblPocet = QtGui.QLabel(self.grpSlozka)
        self.lblPocet.setGeometry(QtCore.QRect(10, 90, 341, 17))
        self.lblPocet.setObjectName("lblPocet")

        self.layoutWidget_2 = QtGui.QWidget(self.grpSlozka)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 50, 451, 29))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.edtSlozka = QtGui.QLineEdit(self.layoutWidget_2)
        self.edtSlozka.setReadOnly(True)
        self.edtSlozka.setFont(font)
        self.edtSlozka.setObjectName("edtSlozka")
        self.horizontalLayout.addWidget(self.edtSlozka)

        self.btnSlozka = QtGui.QPushButton(self.layoutWidget_2)
        self.btnSlozka.setObjectName("btnSlozka")
        self.btnSlozka.clicked.connect(lambda  *args: self.openDir('zmena', self.transGUI('lblSlozka')))
        self.horizontalLayout.addWidget(self.btnSlozka)

        self.grpStart = QtGui.QGroupBox(self.tabResize)
        self.grpStart.setEnabled(False)
        self.grpStart.setGeometry(QtCore.QRect(3, 344, 471, 71))
        self.grpStart.setObjectName("grpStart")

        self.layoutWidget_3 = QtGui.QWidget(self.grpStart)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 30, 451, 29))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.btnStart = QtGui.QPushButton(self.layoutWidget_3)
        self.btnStart.setObjectName("btnStart")
        self.btnStart.clicked.connect(self.resizeImg)
        self.horizontalLayout_2.addWidget(self.btnStart)

        self.progress = QtGui.QProgressBar(self.layoutWidget_3)
        self.progress.setProperty("value", 0)
        self.progress.setTextVisible(True)
        self.progress.setObjectName("progress")
        self.progress.valueChanged.connect(self.threadFinished)
        self.horizontalLayout_2.addWidget(self.progress)

        self.grpUprava = QtGui.QGroupBox(self.tabResize)
        self.grpUprava.setEnabled(False)
        self.grpUprava.setGeometry(QtCore.QRect(3, 140, 469, 116))
        self.grpUprava.setObjectName("grpUprava")

        self.lblPozn = QtGui.QLabel(self.grpUprava)
        self.lblPozn.setGeometry(QtCore.QRect(10, 90, 341, 17))
        self.lblPozn.setFont(logFont)
        self.lblPozn.setObjectName("lblPozn")

        self.layoutWidget_4 = QtGui.QWidget(self.grpUprava)
        self.layoutWidget_4.setGeometry(QtCore.QRect(10, 30, 451, 52))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget_4)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.lblVyska = QtGui.QLabel(self.layoutWidget_4)
        self.lblVyska.setObjectName("lblVyska")
        self.gridLayout.addWidget(self.lblVyska, 0, 0, 1, 1)

        self.lblKvalita = QtGui.QLabel(self.layoutWidget_4)
        self.lblKvalita.setObjectName("lblKvalita")
        self.gridLayout.addWidget(self.lblKvalita, 0, 1, 1, 1)

        self.lblPrefix = QtGui.QLabel(self.layoutWidget_4)
        self.lblPrefix.setObjectName("lblPrefix")
        self.gridLayout.addWidget(self.lblPrefix, 0, 2, 1, 1)

        self.spnVyska = QtGui.QSpinBox(self.layoutWidget_4)
        self.spnVyska.setMinimum(10)
        self.spnVyska.setMaximum(10000)
        self.spnVyska.setProperty("value", 600)
        self.spnVyska.setObjectName("spnVyska")
        self.gridLayout.addWidget(self.spnVyska, 1, 0, 1, 1)

        self.spnKvalita = QtGui.QSpinBox(self.layoutWidget_4)
        self.spnKvalita.setMinimum(10)
        self.spnKvalita.setMaximum(100)
        self.spnKvalita.setSingleStep(5)
        self.spnKvalita.setProperty("value", 85)
        self.spnKvalita.setObjectName("spnKvalita")
        self.gridLayout.addWidget(self.spnKvalita, 1, 1, 1, 1)

        self.edtPrefix = QtGui.QLineEdit(self.layoutWidget_4)
        self.edtPrefix.setObjectName("edtPrefix")
        self.gridLayout.addWidget(self.edtPrefix, 1, 2, 1, 1)

        self.tabWidget.addTab(self.tabResize, "")
        # Konec tab úprava fotek

        # Tab přenos souborů
        self.tabCopy = QtGui.QWidget()
        self.tabCopy.setObjectName("tabCopy")

        self.grpZdroj = QtGui.QGroupBox(self.tabCopy)
        self.grpZdroj.setGeometry(QtCore.QRect(4, 10, 469, 91))
        self.grpZdroj.setObjectName("grpZdroj")

        self.lblZdroj = QtGui.QLabel(self.grpZdroj)
        self.lblZdroj.setGeometry(QtCore.QRect(10, 30, 201, 17))
        self.lblZdroj.setObjectName("lblZdroj")

        self.layoutWidget_5 = QtGui.QWidget(self.grpZdroj)
        self.layoutWidget_5.setGeometry(QtCore.QRect(10, 50, 451, 29))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.edtZdroj = QtGui.QLineEdit(self.layoutWidget_5)
        self.edtZdroj.setReadOnly(True)
        self.edtZdroj.setFont(font)
        self.edtZdroj.setObjectName("edtZdroj")
        self.horizontalLayout_4.addWidget(self.edtZdroj)

        self.btnZdroj = QtGui.QPushButton(self.layoutWidget_5)
        self.btnZdroj.setObjectName("btnZdroj")
        self.btnZdroj.clicked.connect(lambda  *args: self.openDir('zdroj', self.transGUI('lblSlozka')))
        self.horizontalLayout_4.addWidget(self.btnZdroj)

        self.grpCil = QtGui.QGroupBox(self.tabCopy)
        self.grpCil.setGeometry(QtCore.QRect(4, 110, 469, 91))
        self.grpCil.setEnabled(False)
        self.grpCil.setObjectName("grpCil")

        self.lblCil = QtGui.QLabel(self.grpCil)
        self.lblCil.setGeometry(QtCore.QRect(10, 30, 201, 17))
        self.lblCil.setObjectName("lblCil")

        self.layoutWidget_6 = QtGui.QWidget(self.grpCil)
        self.layoutWidget_6.setGeometry(QtCore.QRect(10, 50, 451, 29))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.layoutWidget_6)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        self.edtCil = QtGui.QLineEdit(self.layoutWidget_6)
        self.edtCil.setReadOnly(True)
        self.edtCil.setFont(font)
        self.edtCil.setObjectName("edtCil")
        self.horizontalLayout_5.addWidget(self.edtCil)

        self.btnCil = QtGui.QPushButton(self.layoutWidget_6)
        self.btnCil.setObjectName("btnCil")
        self.btnCil.clicked.connect(lambda  *args: self.openDir('cil', self.transGUI('lblSlozka')))
        self.horizontalLayout_5.addWidget(self.btnCil)

        self.grpPrenos = QtGui.QGroupBox(self.tabCopy)
        self.grpPrenos.setEnabled(False)
        self.grpPrenos.setGeometry(QtCore.QRect(4, 210, 469, 71))
        self.grpPrenos.setObjectName("grpPrenos")

        self.layoutWidget_7 = QtGui.QWidget(self.grpPrenos)
        self.layoutWidget_7.setGeometry(QtCore.QRect(10, 30, 451, 29))
        self.layoutWidget_7.setObjectName("layoutWidget_7")
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.layoutWidget_7)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        self.btnPrenos = QtGui.QPushButton(self.layoutWidget_7)
        self.btnPrenos.setObjectName("btnPrenos")
        self.btnPrenos.clicked.connect(self.copyImg)
        self.horizontalLayout_6.addWidget(self.btnPrenos)

        self.progPrenos = QtGui.QProgressBar(self.layoutWidget_7)
        self.progPrenos.setProperty("value", 0)
        self.progPrenos.setTextVisible(True)
        self.progPrenos.setObjectName("progPrenos")
        self.progPrenos.valueChanged.connect(self.threadFinished)
        self.horizontalLayout_6.addWidget(self.progPrenos)

        self.lblLog = QtGui.QLabel(self.tabCopy)
        self.lblLog.setGeometry(QtCore.QRect(6, 300, 67, 17))
        self.lblLog.setObjectName("lblLog")

        self.lstLog = QtGui.QListWidget(self.tabCopy)
        self.lstLog.setGeometry(QtCore.QRect(6, 319, 465, 101))
        self.lstLog.setFont(logFont)
        self.lstLog.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.lstLog.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.lstLog.setObjectName("lstLog")

        self.tabWidget.addTab(self.tabCopy, "")
        # Konec Tab přenos souborů

        # Tab nastavení
        self.tabSetting = QtGui.QWidget()
        self.tabSetting.setObjectName("tabSetting")
        self.verticalLayoutWidget = QtGui.QWidget(self.tabSetting)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(5, 10, 465, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.grpSetting = QtGui.QGroupBox(self.verticalLayoutWidget)
        self.grpSetting.setObjectName("grpSetting")
        self.widget = QtGui.QWidget(self.grpSetting)
        self.widget.setGeometry(QtCore.QRect(30, 40, 40, 60))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtGui.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lblCzech = QtGui.QLabel(self.widget)
        self.lblCzech.setText("")
        self.lblCzech.setPixmap(QtGui.QPixmap(":icons/inc/cz.png"))
        self.lblCzech.setObjectName("lblCzech")
        self.gridLayout_2.addWidget(self.lblCzech, 0, 0, 1, 1)
        self.rbCzech = QtGui.QRadioButton(self.widget)
        if self.langID == 'cs':
            self.rbCzech.setChecked(True)
        self.rbCzech.setObjectName("rbCzech")
        self.rbCzech.clicked.connect(lambda  *args: self.changeLang('cs'))
        self.gridLayout_2.addWidget(self.rbCzech, 0, 1, 1, 1)
        self.lblEng = QtGui.QLabel(self.widget)
        self.lblEng.setText("")
        self.lblEng.setPixmap(QtGui.QPixmap(":icons/inc/en.png"))
        self.lblEng.setObjectName("lblEng")
        self.gridLayout_2.addWidget(self.lblEng, 1, 0, 1, 1)
        self.rbEng = QtGui.QRadioButton(self.widget)
        if self.langID == 'en':
            self.rbEng.setChecked(True)
        self.rbEng.setObjectName("rbEng")
        self.rbEng.clicked.connect(lambda  *args: self.changeLang('en'))
        self.gridLayout_2.addWidget(self.rbEng, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.grpSetting)
        self.tabWidget.addTab(self.tabSetting, "")
        # Konec Tab nastavení

        MainWindow.setCentralWidget(self.centralWidget)

        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        self.statusBar.setFont(logFont)
        self.statusBar.showMessage("2015-2016 © Miroslav Suchánek   |   msuchos@gmail.com")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi()

        MainWindow.setWindowIcon(QtGui.QIcon(':icons/inc/my-icon.png'))
        MainWindow.setWindowTitle("pyFotoResize v2.0")
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Funkce změny jazyka GUI
    def changeLang(self, idL):
        self.langID = idL
        self.rootElem.set('active', idL)
        self.langXMLfile.write(self.transFilePath, encoding='utf-8')
        self.retranslateUi()

    # Funkce získání překladů GUI z XML
    def transGUI(self, componentName):
        allElem = self.langXMLfile.findall('.//lang')
        for elem in allElem:
            if elem.get('id') == self.langID:
                for child in elem:
                    if child.tag == componentName:
                        return child.text

    # Funkce přidání textů a popisků do GUI aplikace.
    def retranslateUi(self):
        self.grpStart.setTitle(self.transGUI('grpStart'))
        self.btnStart.setText(self.transGUI('btnStart'))
        self.btnStart.setToolTip(self.transGUI('btnStartTool'))
        self.grpSlozka.setTitle(self.transGUI('grpSlozka'))
        self.lblSlozka.setText(self.transGUI('lblSlozka'))
        self.lblPocet.setText(self.transGUI('lblPocet'))
        self.btnSlozka.setText(self.transGUI('btnSlozka'))
        self.btnSlozka.setToolTip(self.transGUI('btnSlozkaTool'))
        self.grpUprava.setTitle(self.transGUI('grpUprava'))
        self.lblPozn.setText(self.transGUI('lblPozn'))
        self.lblVyska.setText(self.transGUI('lblVyska'))
        self.lblKvalita.setText(self.transGUI('lblKvalita'))
        self.lblPrefix.setText(self.transGUI('lblPrefix'))
        self.edtPrefix.setText(self.transGUI('edtPrefix'))
        self.btnExit.setText(self.transGUI('btnExit'))
        self.btnExit.setToolTip(self.transGUI('btnExitTool'))
        self.lblCC.setText(self.transGUI('lblCC'))
        self.lblCC.setToolTip(self.transGUI('lblCCTool'))
        self.lblPy.setText(self.transGUI('lblPy'))
        self.lblPy.setToolTip(self.transGUI('lblPyTool'))
        self.lblGit.setText(self.transGUI('lblGit'))
        self.lblGit.setToolTip(self.transGUI('lblGitTool'))
        self.grpWater.setTitle(self.transGUI('grpWater'))
        self.lblWater.setText(self.transGUI('lblWater'))
        self.edtWater.setText(self.transGUI('edtWater'))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabResize), self.transGUI('tabResize'))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCopy), self.transGUI('tabCopy'))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSetting), self.transGUI('tabSetting'))
        self.grpZdroj.setTitle(self.transGUI('grpZdroj'))
        self.lblZdroj.setText(self.transGUI('lblZdroj'))
        self.btnZdroj.setText(self.transGUI('btnZdroj'))
        self.btnZdroj.setToolTip(self.transGUI('btnZdrojTool'))
        self.grpCil.setTitle(self.transGUI('grpCil'))
        self.lblCil.setText(self.transGUI('lblCil'))
        self.btnCil.setText(self.transGUI('btnCil'))
        self.btnCil.setToolTip(self.transGUI('btnCilTool'))
        self.grpPrenos.setTitle(self.transGUI('grpPrenos'))
        self.btnPrenos.setText(self.transGUI('btnPrenos'))
        self.btnPrenos.setToolTip(self.transGUI('btnPrenosTool'))
        self.lblLog.setText(self.transGUI('lblLog'))
        self.grpSetting.setTitle(self.transGUI('grpSetting'))
        self.rbCzech.setText(self.transGUI('rbCzech'))
        self.rbEng.setText(self.transGUI('rbEng'))

    def openDir(self):
        pass

    def resizeImg(self):
        pass

    def copyImg(self):
        pass

    def getCopyImg(self):
        pass

    def addWatermark(self):
        pass

    def setItemToList(self):
        pass

    def getInfo(self):
        pass

    def progresUpdate(self):
        pass

    def threadFinished(self):
        pass

    def defaultStatus(self):
        pass

    import myicons_rc