# -*- coding: utf-8 -*-

import sys, os, xml.etree.ElementTree as etree
from PySide import QtCore, QtGui
from translategui_xml import translategui_xml

# Uživatelské prostředí aplikace
class fotoResizeGUI(QtGui.QWidget):

    applicationPath = None
    translator = None

    # Funkce inicialzace aplikace.
    def __init__(self):
        self.applicationPath = sys.path[0]
        self.translator = translategui_xml(os.path.join(self.applicationPath, 'inc', 'translate.xml'))

    # Sestavení GUI
    def createGUI(self, MainWindow):

        # Hlavní okno
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(492, 570)
        MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")

        # Nastavení písma
        font = QtGui.QFont()
        font.setPointSize(10)
        logFont = QtGui.QFont()
        logFont.setPointSize(9)

        # Tlačítko Zavřít
        self.btnExit = QtGui.QPushButton(self.centralWidget)
        self.btnExit.setGeometry(QtCore.QRect(370, 480, 99, 27))
        self.btnExit.setObjectName("btnExit")
        self.btnExit.clicked.connect(QtGui.qApp.quit)

        # Tlačítko licence Creative Commons
        self.lblCC = QtGui.QLabel(self.centralWidget)
        self.lblCC.setGeometry(QtCore.QRect(15, 478, 91, 31))
        self.lblCC.setOpenExternalLinks(True)
        self.lblCC.setObjectName("lblCC")

        # Tlačítko Python Powered
        self.lblPy = QtGui.QLabel(self.centralWidget)
        self.lblPy.setGeometry(QtCore.QRect(125, 478, 78, 31))
        self.lblPy.setOpenExternalLinks(True)
        self.lblPy.setObjectName("lblPy")

        # Tlačítko GitHub
        self.lblGit = QtGui.QLabel(self.centralWidget)
        self.lblGit.setGeometry(QtCore.QRect(221, 478, 32, 32))
        self.lblGit.setOpenExternalLinks(True)
        self.lblGit.setObjectName("lblGit")

        # Panel sekcí
        self.tabWidget = QtGui.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(5, 5, 481, 461))
        self.tabWidget.setMouseTracking(True)
        self.tabWidget.setObjectName("tabWidget")

        ###########################################################################
        # Sekce /úprava fotek/
        ###########################################################################
        self.tabResize = QtGui.QWidget()
        self.tabResize.setObjectName("tabResize")

        # GroupBox vodoznaku
        self.grpWater = QtGui.QGroupBox(self.tabResize)
        self.grpWater.setEnabled(False)
        self.grpWater.setGeometry(QtCore.QRect(3, 270, 469, 65))
        self.grpWater.setCheckable(True)
        self.grpWater.setChecked(False)
        self.grpWater.setObjectName("grpWater")

        # Layouty vodoznaku
        self.layoutWidget = QtGui.QWidget(self.grpWater)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 451, 29))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        # Label vodoznaku
        self.lblWater = QtGui.QLabel(self.layoutWidget)
        self.lblWater.setObjectName("lblWater")
        self.horizontalLayout_3.addWidget(self.lblWater)

        # Edit vodoznaku
        self.edtWater = QtGui.QLineEdit(self.layoutWidget)
        self.edtWater.setObjectName("edtWater")
        self.horizontalLayout_3.addWidget(self.edtWater)

        # GroupBox složky fotek
        self.grpSlozka = QtGui.QGroupBox(self.tabResize)
        self.grpSlozka.setGeometry(QtCore.QRect(3, 17, 469, 117))
        self.grpSlozka.setObjectName("grpSlozka")

        # Label složky fotek
        self.lblSlozka = QtGui.QLabel(self.grpSlozka)
        self.lblSlozka.setGeometry(QtCore.QRect(10, 30, 201, 17))
        self.lblSlozka.setObjectName("lblSlozka")

        # Label počtu fotek
        self.lblPocet = QtGui.QLabel(self.grpSlozka)
        self.lblPocet.setGeometry(QtCore.QRect(10, 90, 341, 17))
        self.lblPocet.setObjectName("lblPocet")

        # Layouty složky fotek
        self.layoutWidget_2 = QtGui.QWidget(self.grpSlozka)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 50, 451, 29))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Edit složky fotek
        self.edtSlozka = QtGui.QLineEdit(self.layoutWidget_2)
        self.edtSlozka.setReadOnly(True)
        self.edtSlozka.setFont(font)
        self.edtSlozka.setObjectName("edtSlozka")
        self.horizontalLayout.addWidget(self.edtSlozka)

        # Tlačítko /Procházet/ složky fotek
        self.btnSlozka = QtGui.QPushButton(self.layoutWidget_2)
        self.btnSlozka.setObjectName("btnSlozka")
        self.btnSlozka.clicked.connect(lambda  *args: self.openDir('zmena', self.translator.translate('lblSlozka')))
        self.horizontalLayout.addWidget(self.btnSlozka)

        # GroupBox procesu úprav
        self.grpStart = QtGui.QGroupBox(self.tabResize)
        self.grpStart.setEnabled(False)
        self.grpStart.setGeometry(QtCore.QRect(3, 344, 469, 71))
        self.grpStart.setObjectName("grpStart")

        # Layouty procesu úprav
        self.layoutWidget_3 = QtGui.QWidget(self.grpStart)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 30, 451, 29))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        # Tlačítko /Strat/ procesu úprav
        self.btnStart = QtGui.QPushButton(self.layoutWidget_3)
        self.btnStart.setObjectName("btnStart")
        self.btnStart.clicked.connect(self.resizeImg)
        self.horizontalLayout_2.addWidget(self.btnStart)

        # ProgresBar procesu úprav
        self.progress = QtGui.QProgressBar(self.layoutWidget_3)
        self.progress.setProperty("value", 0)
        self.progress.setTextVisible(True)
        self.progress.setObjectName("progress")
        self.progress.valueChanged.connect(self.threadFinished)
        self.horizontalLayout_2.addWidget(self.progress)

        # GroupBox předvolby úprav
        self.grpUprava = QtGui.QGroupBox(self.tabResize)
        self.grpUprava.setEnabled(False)
        self.grpUprava.setGeometry(QtCore.QRect(3, 140, 469, 116))
        self.grpUprava.setObjectName("grpUprava")

        # Label poznámka
        self.lblPozn = QtGui.QLabel(self.grpUprava)
        self.lblPozn.setGeometry(QtCore.QRect(10, 90, 341, 17))
        self.lblPozn.setFont(logFont)
        self.lblPozn.setObjectName("lblPozn")

        # Layouty předvolby úprav
        self.layoutWidget_4 = QtGui.QWidget(self.grpUprava)
        self.layoutWidget_4.setGeometry(QtCore.QRect(10, 30, 451, 52))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget_4)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        # Label /Výška (px)/
        self.lblVyska = QtGui.QLabel(self.layoutWidget_4)
        self.lblVyska.setObjectName("lblVyska")
        self.gridLayout.addWidget(self.lblVyska, 0, 0, 1, 1)

        # SpinEdit /Výška/
        self.spnVyska = QtGui.QSpinBox(self.layoutWidget_4)
        self.spnVyska.setMinimum(10)
        self.spnVyska.setMaximum(10000)
        self.spnVyska.setProperty("value", 600)
        self.spnVyska.setObjectName("spnVyska")
        self.gridLayout.addWidget(self.spnVyska, 1, 0, 1, 1)

        # Label /Kvalita (%)/
        self.lblKvalita = QtGui.QLabel(self.layoutWidget_4)
        self.lblKvalita.setObjectName("lblKvalita")
        self.gridLayout.addWidget(self.lblKvalita, 0, 1, 1, 1)

        # SpinEdit /Kvalita/
        self.spnKvalita = QtGui.QSpinBox(self.layoutWidget_4)
        self.spnKvalita.setMinimum(10)
        self.spnKvalita.setMaximum(100)
        self.spnKvalita.setSingleStep(5)
        self.spnKvalita.setProperty("value", 85)
        self.spnKvalita.setObjectName("spnKvalita")
        self.gridLayout.addWidget(self.spnKvalita, 1, 1, 1, 1)

        # Label /Prefix/
        self.lblPrefix = QtGui.QLabel(self.layoutWidget_4)
        self.lblPrefix.setObjectName("lblPrefix")
        self.gridLayout.addWidget(self.lblPrefix, 0, 2, 1, 1)

        # Edit /Prefix/
        self.edtPrefix = QtGui.QLineEdit(self.layoutWidget_4)
        self.edtPrefix.setObjectName("edtPrefix")
        self.gridLayout.addWidget(self.edtPrefix, 1, 2, 1, 1)

        self.tabWidget.addTab(self.tabResize, "")
        #############################################################################
        # Konec sekce /úprava fotek/
        #############################################################################

        #############################################################################
        # Sekce /kopírování souborů/
        #############################################################################
        self.tabCopy = QtGui.QWidget()
        self.tabCopy.setObjectName("tabCopy")

        # GroupBox zdrojové složky
        self.grpZdroj = QtGui.QGroupBox(self.tabCopy)
        self.grpZdroj.setGeometry(QtCore.QRect(4, 10, 467, 91))
        self.grpZdroj.setObjectName("grpZdroj")

        # Label zdrojové složky
        self.lblZdroj = QtGui.QLabel(self.grpZdroj)
        self.lblZdroj.setGeometry(QtCore.QRect(10, 30, 201, 17))
        self.lblZdroj.setObjectName("lblZdroj")

        # Layouty zdrojové složky
        self.layoutWidget_5 = QtGui.QWidget(self.grpZdroj)
        self.layoutWidget_5.setGeometry(QtCore.QRect(10, 50, 451, 29))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        # Edit zdrojové složky
        self.edtZdroj = QtGui.QLineEdit(self.layoutWidget_5)
        self.edtZdroj.setReadOnly(True)
        self.edtZdroj.setFont(font)
        self.edtZdroj.setObjectName("edtZdroj")
        self.horizontalLayout_4.addWidget(self.edtZdroj)

        # Tlačítko /Procházet/ zdrojové složky
        self.btnZdroj = QtGui.QPushButton(self.layoutWidget_5)
        self.btnZdroj.setObjectName("btnZdroj")
        self.btnZdroj.clicked.connect(lambda  *args: self.openDir('zdroj', self.translator.translate('lblSlozka')))
        self.horizontalLayout_4.addWidget(self.btnZdroj)

        # GroupBox cílové složky
        self.grpCil = QtGui.QGroupBox(self.tabCopy)
        self.grpCil.setGeometry(QtCore.QRect(4, 110, 467, 91))
        self.grpCil.setEnabled(False)
        self.grpCil.setObjectName("grpCil")

        # Label cílové složky
        self.lblCil = QtGui.QLabel(self.grpCil)
        self.lblCil.setGeometry(QtCore.QRect(10, 30, 201, 17))
        self.lblCil.setObjectName("lblCil")

        # Layouty cílové složky
        self.layoutWidget_6 = QtGui.QWidget(self.grpCil)
        self.layoutWidget_6.setGeometry(QtCore.QRect(10, 50, 451, 29))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.layoutWidget_6)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        # Edit cílové složky
        self.edtCil = QtGui.QLineEdit(self.layoutWidget_6)
        self.edtCil.setReadOnly(True)
        self.edtCil.setFont(font)
        self.edtCil.setObjectName("edtCil")
        self.horizontalLayout_5.addWidget(self.edtCil)

        # Tlačítko /Procházet/ cílové složky
        self.btnCil = QtGui.QPushButton(self.layoutWidget_6)
        self.btnCil.setObjectName("btnCil")
        self.btnCil.clicked.connect(lambda  *args: self.openDir('cil', self.translator.translate('lblSlozka')))
        self.horizontalLayout_5.addWidget(self.btnCil)

        # GroupBox procesu kopírování
        self.grpPrenos = QtGui.QGroupBox(self.tabCopy)
        self.grpPrenos.setEnabled(False)
        self.grpPrenos.setGeometry(QtCore.QRect(4, 210, 467, 71))
        self.grpPrenos.setObjectName("grpPrenos")

        # Layouty procesu kopírování
        self.layoutWidget_7 = QtGui.QWidget(self.grpPrenos)
        self.layoutWidget_7.setGeometry(QtCore.QRect(10, 30, 451, 29))
        self.layoutWidget_7.setObjectName("layoutWidget_7")
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.layoutWidget_7)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        # Tlačítko /Start/ procesu kopírování
        self.btnPrenos = QtGui.QPushButton(self.layoutWidget_7)
        self.btnPrenos.setObjectName("btnPrenos")
        self.btnPrenos.clicked.connect(self.copyImg)
        self.horizontalLayout_6.addWidget(self.btnPrenos)

        # ProgresBar procesu kopírování
        self.progPrenos = QtGui.QProgressBar(self.layoutWidget_7)
        self.progPrenos.setProperty("value", 0)
        self.progPrenos.setTextVisible(True)
        self.progPrenos.setObjectName("progPrenos")
        self.progPrenos.valueChanged.connect(self.threadFinished)
        self.horizontalLayout_6.addWidget(self.progPrenos)

        # Label logu
        self.lblLog = QtGui.QLabel(self.tabCopy)
        self.lblLog.setGeometry(QtCore.QRect(6, 296, 67, 20))
        self.lblLog.setObjectName("lblLog")

        # List logu
        self.lstLog = QtGui.QListWidget(self.tabCopy)
        self.lstLog.setGeometry(QtCore.QRect(6, 319, 465, 101))
        self.lstLog.setFont(logFont)
        self.lstLog.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.lstLog.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.lstLog.setObjectName("lstLog")

        self.tabWidget.addTab(self.tabCopy, "")
        ###################################################################################
        # Konec sekce /kopírování souborů/
        ###################################################################################

        ###################################################################################
        # Sekce /nastavení/
        ###################################################################################
        self.tabSetting = QtGui.QWidget()
        self.tabSetting.setObjectName("tabSetting")

        # Layouty sekce nastavení
        self.verticalLayoutWidget = QtGui.QWidget(self.tabSetting)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(5, 10, 465, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        # GroupBox jazyka GUI
        self.grpSetting = QtGui.QGroupBox(self.verticalLayoutWidget)
        self.grpSetting.setObjectName("grpSetting")

        # Layouty jazyka GUI
        self.widget = QtGui.QWidget(self.grpSetting)
        self.widget.setGeometry(QtCore.QRect(28, 40, 60, 66))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtGui.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")

        # přepínače jazyka (radiobuttony s vlajkou)
        self.createLangRB([28, 40], [70, 50])

        self.verticalLayout.addWidget(self.grpSetting)
        self.tabWidget.addTab(self.tabSetting, "")
        ######################################################################################
        # Konec sekce /nastavení/
        ######################################################################################

        MainWindow.setCentralWidget(self.centralWidget)

        # StatusBar
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        self.statusBar.setFont(logFont)
        self.statusBar.showMessage("2016 © Miroslav Suchánek   |   pyfotoresize.webnode.cz")
        MainWindow.setStatusBar(self.statusBar)

        # Přiřazení textů GUI
        self.setTranslations()

        MainWindow.setWindowIcon(QtGui.QIcon(':icons/inc/my-icon.png'))
        MainWindow.setWindowTitle("MISU pyFotoResize v2.0")
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Funkce změny jazyka GUI
    def changeLang(self):
        idL = self.translator.allLangID[self.langRadioGroup.checkedId()][0]
        self.translator.changeActiveLangID(idL)
        self.setTranslations()

    def createLangRB(self, lblXY=[], rbXY=[]):
        labelXY = lblXY #[28, 40]
        radioXY = rbXY #[70, 50]
        self.langRadioGroup = QtGui.QButtonGroup()
        self.langRadioGroup.setExclusive(True)
        for i, language in enumerate(self.translator.allLangID):
            lblVlajka = QtGui.QLabel(self.widget)
            lblVlajka.setGeometry(QtCore.QRect(labelXY[0], labelXY[1], 32, 32))
            lblVlajka.setText('')
            lblVlajka.setPixmap(QtGui.QPixmap(language[1]))
            lblVlajka.setObjectName('lbl'+language[0])
            self.gridLayout_2.addWidget(lblVlajka, i, 0, 1, 1)
            self.widget.setGeometry(QtCore.QRect(28, 40, 60, labelXY[1]))
            labelXY[1] += 40

            rbVlajka = QtGui.QRadioButton()
            if self.translator.activeLangID == language[0]:
                rbVlajka.setChecked(True)
            rbVlajka.setGeometry(QtCore.QRect(radioXY[0], radioXY[1], 20, 20))
            rbVlajka.setObjectName('rb'+language[0])
            rbVlajka.clicked.connect(self.changeLang)
            self.langRadioGroup.addButton(rbVlajka, i)
            self.gridLayout_2.addWidget(rbVlajka, i, 1, 1, 1)
            radioXY[1] += 40

            self.verticalLayoutWidget.setGeometry(QtCore.QRect(5, 10, 465, labelXY[1]+20))


    # Funkce nastavení a přiřazení textů a popisků do GUI
    def setTranslations(self):
        self.grpStart.setTitle(self.translator.translate('grpStart'))
        self.btnStart.setText(self.translator.translate('btnStart'))
        self.btnStart.setToolTip(self.translator.translate('btnStartTool'))
        self.grpSlozka.setTitle(self.translator.translate('grpSlozka'))
        self.lblSlozka.setText(self.translator.translate('lblSlozka'))
        self.lblPocet.setText(self.translator.translate('lblPocet'))
        self.btnSlozka.setText(self.translator.translate('btnSlozka'))
        self.btnSlozka.setToolTip(self.translator.translate('btnSlozkaTool'))
        self.grpUprava.setTitle(self.translator.translate('grpUprava'))
        self.lblPozn.setText(self.translator.translate('lblPozn'))
        self.lblVyska.setText(self.translator.translate('lblVyska'))
        self.lblKvalita.setText(self.translator.translate('lblKvalita'))
        self.lblPrefix.setText(self.translator.translate('lblPrefix'))
        self.edtPrefix.setText(self.translator.translate('edtPrefix'))
        self.btnExit.setText(self.translator.translate('btnExit'))
        self.btnExit.setToolTip(self.translator.translate('btnExitTool'))
        self.lblCC.setText(self.translator.translate('lblCC'))
        self.lblCC.setToolTip(self.translator.translate('lblCCTool'))
        self.lblPy.setText(self.translator.translate('lblPy'))
        self.lblPy.setToolTip(self.translator.translate('lblPyTool'))
        self.lblGit.setText(self.translator.translate('lblGit'))
        self.lblGit.setToolTip(self.translator.translate('lblGitTool'))
        self.grpWater.setTitle(self.translator.translate('grpWater'))
        self.lblWater.setText(self.translator.translate('lblWater'))
        self.edtWater.setText(self.translator.translate('edtWater'))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabResize), self.translator.translate('tabResize'))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCopy), self.translator.translate('tabCopy'))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSetting), self.translator.translate('tabSetting'))
        self.grpZdroj.setTitle(self.translator.translate('grpZdroj'))
        self.lblZdroj.setText(self.translator.translate('lblZdroj'))
        self.btnZdroj.setText(self.translator.translate('btnZdroj'))
        self.btnZdroj.setToolTip(self.translator.translate('btnZdrojTool'))
        self.grpCil.setTitle(self.translator.translate('grpCil'))
        self.lblCil.setText(self.translator.translate('lblCil'))
        self.btnCil.setText(self.translator.translate('btnCil'))
        self.btnCil.setToolTip(self.translator.translate('btnCilTool'))
        self.grpPrenos.setTitle(self.translator.translate('grpPrenos'))
        self.btnPrenos.setText(self.translator.translate('btnPrenos'))
        self.btnPrenos.setToolTip(self.translator.translate('btnPrenosTool'))
        self.lblLog.setText(self.translator.translate('lblLog'))
        self.grpSetting.setTitle(self.translator.translate('grpSetting'))

    def openDir(self):
        pass

    def resizeImg(self):
        pass

    def copyImg(self):
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