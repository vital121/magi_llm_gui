# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'magi_llm_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QGroupBox, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPlainTextEdit,
    QPushButton, QRadioButton, QSizePolicy, QStatusBar,
    QTabWidget, QTextEdit, QToolButton, QVBoxLayout,
    QWidget)

class Ui_magi_llm_window(object):
    def setupUi(self, magi_llm_window):
        if not magi_llm_window.objectName():
            magi_llm_window.setObjectName(u"magi_llm_window")
        magi_llm_window.resize(854, 1033)
        font = QFont()
        font.setPointSize(11)
        magi_llm_window.setFont(font)
        self.actionSettings = QAction(magi_llm_window)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionExit = QAction(magi_llm_window)
        self.actionExit.setObjectName(u"actionExit")
        self.actionAbout = QAction(magi_llm_window)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionStop = QAction(magi_llm_window)
        self.actionStop.setObjectName(u"actionStop")
        self.centralwidget = QWidget(magi_llm_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.textgenTab = QTabWidget(self.centralwidget)
        self.textgenTab.setObjectName(u"textgenTab")
        self.textgenTab.setAutoFillBackground(False)
        self.chat_textgenTab = QWidget()
        self.chat_textgenTab.setObjectName(u"chat_textgenTab")
        self.chat_textgenTab.setAutoFillBackground(True)
        self.gridLayout_3 = QGridLayout(self.chat_textgenTab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.chat_modeTextInput = QPlainTextEdit(self.chat_textgenTab)
        self.chat_modeTextInput.setObjectName(u"chat_modeTextInput")
        self.chat_modeTextInput.setMaximumSize(QSize(16777215, 128))
        font1 = QFont()
        font1.setPointSize(12)
        self.chat_modeTextInput.setFont(font1)

        self.gridLayout_3.addWidget(self.chat_modeTextInput, 6, 0, 1, 2)

        self.chatButtonGroup = QFrame(self.chat_textgenTab)
        self.chatButtonGroup.setObjectName(u"chatButtonGroup")
        self.gridLayout_11 = QGridLayout(self.chatButtonGroup)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.chatClearButton = QPushButton(self.chatButtonGroup)
        self.chatClearButton.setObjectName(u"chatClearButton")
        self.chatClearButton.setEnabled(False)

        self.gridLayout_11.addWidget(self.chatClearButton, 0, 2, 1, 1)

        self.chatContinueButton = QPushButton(self.chatButtonGroup)
        self.chatContinueButton.setObjectName(u"chatContinueButton")
        self.chatContinueButton.setEnabled(False)

        self.gridLayout_11.addWidget(self.chatContinueButton, 0, 0, 1, 1)

        self.chatStopButton = QPushButton(self.chatButtonGroup)
        self.chatStopButton.setObjectName(u"chatStopButton")
        self.chatStopButton.setEnabled(False)

        self.gridLayout_11.addWidget(self.chatStopButton, 0, 4, 1, 1)

        self.chatRewindButton = QPushButton(self.chatButtonGroup)
        self.chatRewindButton.setObjectName(u"chatRewindButton")
        self.chatRewindButton.setEnabled(False)

        self.gridLayout_11.addWidget(self.chatRewindButton, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.chatButtonGroup, 8, 1, 1, 1)

        self.chatInputSessionCombo = QComboBox(self.chat_textgenTab)
        self.chatInputSessionCombo.setObjectName(u"chatInputSessionCombo")
        self.chatInputSessionCombo.setMaxCount(128)

        self.gridLayout_3.addWidget(self.chatInputSessionCombo, 4, 0, 1, 2)

        self.chat_modeTextHistory = QTextEdit(self.chat_textgenTab)
        self.chat_modeTextHistory.setObjectName(u"chat_modeTextHistory")
        self.chat_modeTextHistory.setFont(font1)
        self.chat_modeTextHistory.setReadOnly(True)

        self.gridLayout_3.addWidget(self.chat_modeTextHistory, 2, 0, 1, 2)

        self.chatGenerateButton = QPushButton(self.chat_textgenTab)
        self.chatGenerateButton.setObjectName(u"chatGenerateButton")
        self.chatGenerateButton.setEnabled(False)
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setUnderline(False)
        self.chatGenerateButton.setFont(font2)

        self.gridLayout_3.addWidget(self.chatGenerateButton, 8, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.chat_textgenTab)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_8 = QGridLayout(self.groupBox_4)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.instructPresetComboBox = QComboBox(self.groupBox_4)
        self.instructPresetComboBox.setObjectName(u"instructPresetComboBox")

        self.gridLayout_8.addWidget(self.instructPresetComboBox, 0, 1, 1, 1)

        self.instructRadioButton = QRadioButton(self.groupBox_4)
        self.instructRadioButton.setObjectName(u"instructRadioButton")
        self.instructRadioButton.setChecked(True)

        self.gridLayout_8.addWidget(self.instructRadioButton, 0, 0, 1, 1)

        self.characterPresetComboBox = QComboBox(self.groupBox_4)
        self.characterPresetComboBox.setObjectName(u"characterPresetComboBox")

        self.gridLayout_8.addWidget(self.characterPresetComboBox, 0, 3, 1, 2)

        self.label = QLabel(self.groupBox_4)
        self.label.setObjectName(u"label")

        self.gridLayout_8.addWidget(self.label, 1, 0, 1, 1)

        self.charactersRadioButton = QRadioButton(self.groupBox_4)
        self.charactersRadioButton.setObjectName(u"charactersRadioButton")

        self.gridLayout_8.addWidget(self.charactersRadioButton, 0, 2, 1, 1)

        self.awesomePresetComboBox = QComboBox(self.groupBox_4)
        self.awesomePresetComboBox.setObjectName(u"awesomePresetComboBox")

        self.gridLayout_8.addWidget(self.awesomePresetComboBox, 1, 1, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_4, 0, 0, 1, 2)

        self.textgenTab.addTab(self.chat_textgenTab, "")
        self.standard_textgenTab = QWidget()
        self.standard_textgenTab.setObjectName(u"standard_textgenTab")
        self.standard_textgenTab.setAutoFillBackground(True)
        self.gridLayout_6 = QGridLayout(self.standard_textgenTab)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.defaultTextInput = QPlainTextEdit(self.standard_textgenTab)
        self.defaultTextInput.setObjectName(u"defaultTextInput")
        self.defaultTextInput.setFont(font1)

        self.gridLayout_6.addWidget(self.defaultTextInput, 1, 0, 1, 2)

        self.defaultGenerateButton = QPushButton(self.standard_textgenTab)
        self.defaultGenerateButton.setObjectName(u"defaultGenerateButton")
        self.defaultGenerateButton.setEnabled(False)
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.defaultGenerateButton.setFont(font3)

        self.gridLayout_6.addWidget(self.defaultGenerateButton, 2, 0, 1, 1)

        self.standardButtonGroup = QFrame(self.standard_textgenTab)
        self.standardButtonGroup.setObjectName(u"standardButtonGroup")
        self.gridLayout_12 = QGridLayout(self.standardButtonGroup)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.defaultContinueButton = QPushButton(self.standardButtonGroup)
        self.defaultContinueButton.setObjectName(u"defaultContinueButton")
        self.defaultContinueButton.setEnabled(False)

        self.gridLayout_12.addWidget(self.defaultContinueButton, 0, 0, 1, 1)

        self.defaultClearButton = QPushButton(self.standardButtonGroup)
        self.defaultClearButton.setObjectName(u"defaultClearButton")
        self.defaultClearButton.setEnabled(False)

        self.gridLayout_12.addWidget(self.defaultClearButton, 0, 1, 1, 1)

        self.defaultStopButton = QPushButton(self.standardButtonGroup)
        self.defaultStopButton.setObjectName(u"defaultStopButton")
        self.defaultStopButton.setEnabled(False)

        self.gridLayout_12.addWidget(self.defaultStopButton, 0, 2, 1, 1)


        self.gridLayout_6.addWidget(self.standardButtonGroup, 2, 1, 1, 1)

        self.default_modeTextHistory = QTextEdit(self.standard_textgenTab)
        self.default_modeTextHistory.setObjectName(u"default_modeTextHistory")
        self.default_modeTextHistory.setFont(font1)
        self.default_modeTextHistory.setReadOnly(True)

        self.gridLayout_6.addWidget(self.default_modeTextHistory, 0, 0, 1, 2)

        self.textgenTab.addTab(self.standard_textgenTab, "")
        self.notebook_textgenTab = QWidget()
        self.notebook_textgenTab.setObjectName(u"notebook_textgenTab")
        self.notebook_textgenTab.setAutoFillBackground(True)
        self.gridLayout_2 = QGridLayout(self.notebook_textgenTab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.notebookGenerateButton = QPushButton(self.notebook_textgenTab)
        self.notebookGenerateButton.setObjectName(u"notebookGenerateButton")
        self.notebookGenerateButton.setEnabled(False)
        self.notebookGenerateButton.setFont(font3)

        self.gridLayout_2.addWidget(self.notebookGenerateButton, 1, 0, 1, 1)

        self.notebookButtonGroup = QFrame(self.notebook_textgenTab)
        self.notebookButtonGroup.setObjectName(u"notebookButtonGroup")
        self.gridLayout_9 = QGridLayout(self.notebookButtonGroup)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.notebookClearButton = QPushButton(self.notebookButtonGroup)
        self.notebookClearButton.setObjectName(u"notebookClearButton")
        self.notebookClearButton.setEnabled(False)

        self.gridLayout_9.addWidget(self.notebookClearButton, 0, 1, 1, 1)

        self.notebookContinueButton = QPushButton(self.notebookButtonGroup)
        self.notebookContinueButton.setObjectName(u"notebookContinueButton")
        self.notebookContinueButton.setEnabled(False)

        self.gridLayout_9.addWidget(self.notebookContinueButton, 0, 0, 1, 1)

        self.notebookStopButton = QPushButton(self.notebookButtonGroup)
        self.notebookStopButton.setObjectName(u"notebookStopButton")
        self.notebookStopButton.setEnabled(False)

        self.gridLayout_9.addWidget(self.notebookStopButton, 0, 2, 1, 1)


        self.gridLayout_2.addWidget(self.notebookButtonGroup, 1, 1, 1, 1)

        self.notebook_modeTextHistory = QTextEdit(self.notebook_textgenTab)
        self.notebook_modeTextHistory.setObjectName(u"notebook_modeTextHistory")
        self.notebook_modeTextHistory.setFont(font1)
        self.notebook_modeTextHistory.setAcceptRichText(False)

        self.gridLayout_2.addWidget(self.notebook_modeTextHistory, 0, 0, 1, 2)

        self.textgenTab.addTab(self.notebook_textgenTab, "")
        self.settingsTab = QWidget()
        self.settingsTab.setObjectName(u"settingsTab")
        self.settingsTab.setAutoFillBackground(True)
        self.gridLayout_4 = QGridLayout(self.settingsTab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox_2 = QGroupBox(self.settingsTab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_5 = QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_28 = QLabel(self.groupBox_2)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_5.addWidget(self.label_28, 4, 0, 1, 1)

        self.streamEnabledCheck = QCheckBox(self.groupBox_2)
        self.streamEnabledCheck.setObjectName(u"streamEnabledCheck")
        self.streamEnabledCheck.setChecked(True)

        self.gridLayout_5.addWidget(self.streamEnabledCheck, 0, 0, 1, 1)

        self.RWKVcppModelSelect = QToolButton(self.groupBox_2)
        self.RWKVcppModelSelect.setObjectName(u"RWKVcppModelSelect")

        self.gridLayout_5.addWidget(self.RWKVcppModelSelect, 6, 2, 1, 1)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_5.addWidget(self.label_3, 5, 0, 1, 1)

        self.logChatCheck = QCheckBox(self.groupBox_2)
        self.logChatCheck.setObjectName(u"logChatCheck")
        self.logChatCheck.setChecked(False)

        self.gridLayout_5.addWidget(self.logChatCheck, 0, 1, 1, 1)

        self.line = QFrame(self.groupBox_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line, 3, 0, 1, 2)

        self.rwkvCppModelPath = QLineEdit(self.groupBox_2)
        self.rwkvCppModelPath.setObjectName(u"rwkvCppModelPath")

        self.gridLayout_5.addWidget(self.rwkvCppModelPath, 6, 1, 1, 1)

        self.exllamaModelSelect = QToolButton(self.groupBox_2)
        self.exllamaModelSelect.setObjectName(u"exllamaModelSelect")

        self.gridLayout_5.addWidget(self.exllamaModelSelect, 5, 2, 1, 1)

        self.cppModelPath = QLineEdit(self.groupBox_2)
        self.cppModelPath.setObjectName(u"cppModelPath")

        self.gridLayout_5.addWidget(self.cppModelPath, 4, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_5.addWidget(self.label_2, 6, 0, 1, 1)

        self.cppModelSelect = QToolButton(self.groupBox_2)
        self.cppModelSelect.setObjectName(u"cppModelSelect")
        self.cppModelSelect.setArrowType(Qt.NoArrow)

        self.gridLayout_5.addWidget(self.cppModelSelect, 4, 2, 1, 1)

        self.exllamaModelPath = QLineEdit(self.groupBox_2)
        self.exllamaModelPath.setObjectName(u"exllamaModelPath")

        self.gridLayout_5.addWidget(self.exllamaModelPath, 5, 1, 1, 1)

        self.sendStopStringCheck = QCheckBox(self.groupBox_2)
        self.sendStopStringCheck.setObjectName(u"sendStopStringCheck")
        self.sendStopStringCheck.setChecked(True)

        self.gridLayout_5.addWidget(self.sendStopStringCheck, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_2, 2, 0, 1, 2)

        self.settingsPathSaveButton = QPushButton(self.settingsTab)
        self.settingsPathSaveButton.setObjectName(u"settingsPathSaveButton")

        self.gridLayout_4.addWidget(self.settingsPathSaveButton, 4, 0, 1, 2)

        self.groupBox_3 = QGroupBox(self.settingsTab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.themeDarkCheck = QRadioButton(self.groupBox_3)
        self.themeDarkCheck.setObjectName(u"themeDarkCheck")
        self.themeDarkCheck.setChecked(False)

        self.verticalLayout_2.addWidget(self.themeDarkCheck)

        self.themeLightCheck = QRadioButton(self.groupBox_3)
        self.themeLightCheck.setObjectName(u"themeLightCheck")

        self.verticalLayout_2.addWidget(self.themeLightCheck)

        self.themeNativeCheck = QRadioButton(self.groupBox_3)
        self.themeNativeCheck.setObjectName(u"themeNativeCheck")
        self.themeNativeCheck.setChecked(True)

        self.verticalLayout_2.addWidget(self.themeNativeCheck)


        self.gridLayout_4.addWidget(self.groupBox_3, 0, 1, 1, 1)

        self.backendGroup = QGroupBox(self.settingsTab)
        self.backendGroup.setObjectName(u"backendGroup")
        self.gridLayout_10 = QGridLayout(self.backendGroup)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.loadModelButton = QPushButton(self.backendGroup)
        self.loadModelButton.setObjectName(u"loadModelButton")

        self.gridLayout_10.addWidget(self.loadModelButton, 9, 0, 1, 1)

        self.cppCheck = QRadioButton(self.backendGroup)
        self.cppCheck.setObjectName(u"cppCheck")
        self.cppCheck.setChecked(True)

        self.gridLayout_10.addWidget(self.cppCheck, 0, 0, 1, 1)

        self.rwkvCppCheck = QRadioButton(self.backendGroup)
        self.rwkvCppCheck.setObjectName(u"rwkvCppCheck")

        self.gridLayout_10.addWidget(self.rwkvCppCheck, 4, 0, 1, 1)

        self.unloadModelButton = QPushButton(self.backendGroup)
        self.unloadModelButton.setObjectName(u"unloadModelButton")
        self.unloadModelButton.setEnabled(False)

        self.gridLayout_10.addWidget(self.unloadModelButton, 9, 1, 1, 1)

        self.tsServerCheck = QRadioButton(self.backendGroup)
        self.tsServerCheck.setObjectName(u"tsServerCheck")
        self.tsServerCheck.setChecked(False)

        self.gridLayout_10.addWidget(self.tsServerCheck, 8, 0, 1, 1)

        self.exllamaCheck = QRadioButton(self.backendGroup)
        self.exllamaCheck.setObjectName(u"exllamaCheck")
        self.exllamaCheck.setChecked(False)

        self.gridLayout_10.addWidget(self.exllamaCheck, 2, 0, 1, 1)

        self.cppServerCheck = QRadioButton(self.backendGroup)
        self.cppServerCheck.setObjectName(u"cppServerCheck")

        self.gridLayout_10.addWidget(self.cppServerCheck, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.backendGroup, 0, 0, 1, 1)

        self.groupBox = QGroupBox(self.settingsTab)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_7 = QGridLayout(self.groupBox)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.customResponsePrefix = QLineEdit(self.groupBox)
        self.customResponsePrefix.setObjectName(u"customResponsePrefix")

        self.gridLayout_7.addWidget(self.customResponsePrefix, 3, 2, 1, 1)

        self.yourNameLine = QLineEdit(self.groupBox)
        self.yourNameLine.setObjectName(u"yourNameLine")

        self.gridLayout_7.addWidget(self.yourNameLine, 1, 2, 1, 1)

        self.customResponsePrefixCheck = QCheckBox(self.groupBox)
        self.customResponsePrefixCheck.setObjectName(u"customResponsePrefixCheck")

        self.gridLayout_7.addWidget(self.customResponsePrefixCheck, 3, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_7.addWidget(self.label_4, 1, 0, 1, 1)

        self.botNameLine = QLineEdit(self.groupBox)
        self.botNameLine.setObjectName(u"botNameLine")

        self.gridLayout_7.addWidget(self.botNameLine, 2, 2, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_7.addWidget(self.label_5, 2, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox, 3, 0, 1, 2)

        self.textgenTab.addTab(self.settingsTab, "")

        self.gridLayout.addWidget(self.textgenTab, 0, 0, 1, 1)

        magi_llm_window.setCentralWidget(self.centralwidget)
        self.llm_menubar = QMenuBar(magi_llm_window)
        self.llm_menubar.setObjectName(u"llm_menubar")
        self.llm_menubar.setGeometry(QRect(0, 0, 854, 27))
        self.menuFile = QMenu(self.llm_menubar)
        self.menuFile.setObjectName(u"menuFile")
        magi_llm_window.setMenuBar(self.llm_menubar)
        self.statusbar = QStatusBar(magi_llm_window)
        self.statusbar.setObjectName(u"statusbar")
        magi_llm_window.setStatusBar(self.statusbar)

        self.llm_menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addAction(self.actionExit)

        self.retranslateUi(magi_llm_window)
        self.defaultClearButton.clicked.connect(self.default_modeTextHistory.clear)
        self.notebookClearButton.clicked.connect(self.notebook_modeTextHistory.clear)

        self.textgenTab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(magi_llm_window)
    # setupUi

    def retranslateUi(self, magi_llm_window):
        magi_llm_window.setWindowTitle(QCoreApplication.translate("magi_llm_window", u"Magi LLM", None))
        self.actionSettings.setText(QCoreApplication.translate("magi_llm_window", u"Parameters", None))
        self.actionExit.setText(QCoreApplication.translate("magi_llm_window", u"Exit", None))
        self.actionAbout.setText(QCoreApplication.translate("magi_llm_window", u"About", None))
        self.actionStop.setText(QCoreApplication.translate("magi_llm_window", u"Stop", None))
#if QT_CONFIG(tooltip)
        self.textgenTab.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.chat_modeTextInput.setToolTip(QCoreApplication.translate("magi_llm_window", u"User chat input", None))
#endif // QT_CONFIG(tooltip)
        self.chat_modeTextInput.setPlainText("")
        self.chat_modeTextInput.setPlaceholderText(QCoreApplication.translate("magi_llm_window", u"Type something here", None))
#if QT_CONFIG(tooltip)
        self.chatClearButton.setToolTip(QCoreApplication.translate("magi_llm_window", u"Clear the output history", None))
#endif // QT_CONFIG(tooltip)
        self.chatClearButton.setText(QCoreApplication.translate("magi_llm_window", u"Clear", None))
#if QT_CONFIG(tooltip)
        self.chatContinueButton.setToolTip(QCoreApplication.translate("magi_llm_window", u"Continue the last generation", None))
#endif // QT_CONFIG(tooltip)
        self.chatContinueButton.setText(QCoreApplication.translate("magi_llm_window", u"Continue", None))
#if QT_CONFIG(tooltip)
        self.chatStopButton.setToolTip(QCoreApplication.translate("magi_llm_window", u"Stop generation", None))
#endif // QT_CONFIG(tooltip)
        self.chatStopButton.setText(QCoreApplication.translate("magi_llm_window", u"Stop", None))
#if QT_CONFIG(tooltip)
        self.chatRewindButton.setToolTip(QCoreApplication.translate("magi_llm_window", u"Rewinds the chat 1 turn", None))
#endif // QT_CONFIG(tooltip)
        self.chatRewindButton.setText(QCoreApplication.translate("magi_llm_window", u"Rewind", None))
#if QT_CONFIG(tooltip)
        self.chatInputSessionCombo.setToolTip(QCoreApplication.translate("magi_llm_window", u"Saved chat inputs from session", None))
#endif // QT_CONFIG(tooltip)
        self.chatInputSessionCombo.setPlaceholderText(QCoreApplication.translate("magi_llm_window", u"User input history", None))
        self.chat_modeTextHistory.setPlaceholderText(QCoreApplication.translate("magi_llm_window", u"Output goes here", None))
#if QT_CONFIG(tooltip)
        self.chatGenerateButton.setToolTip(QCoreApplication.translate("magi_llm_window", u"Send (CTRL+Enter)", None))
#endif // QT_CONFIG(tooltip)
        self.chatGenerateButton.setText(QCoreApplication.translate("magi_llm_window", u"Generate", None))
#if QT_CONFIG(shortcut)
        self.chatGenerateButton.setShortcut(QCoreApplication.translate("magi_llm_window", u"Ctrl+Return", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox_4.setTitle("")
#if QT_CONFIG(tooltip)
        self.instructPresetComboBox.setToolTip(QCoreApplication.translate("magi_llm_window", u"Select instruct format", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.instructRadioButton.setToolTip(QCoreApplication.translate("magi_llm_window", u"Use instruct mode (from presets/instruct folder)", None))
#endif // QT_CONFIG(tooltip)
        self.instructRadioButton.setText(QCoreApplication.translate("magi_llm_window", u"Instruct:", None))
#if QT_CONFIG(tooltip)
        self.characterPresetComboBox.setToolTip(QCoreApplication.translate("magi_llm_window", u"Select a character", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("magi_llm_window", u"Awesome prompts:", None))
#if QT_CONFIG(tooltip)
        self.charactersRadioButton.setToolTip(QCoreApplication.translate("magi_llm_window", u"Use character/chat mode (from presets/characters folder)", None))
#endif // QT_CONFIG(tooltip)
        self.charactersRadioButton.setText(QCoreApplication.translate("magi_llm_window", u"Characters:", None))
#if QT_CONFIG(tooltip)
        self.awesomePresetComboBox.setToolTip(QCoreApplication.translate("magi_llm_window", u"Select a preset prompt", None))
#endif // QT_CONFIG(tooltip)
        self.textgenTab.setTabText(self.textgenTab.indexOf(self.chat_textgenTab), QCoreApplication.translate("magi_llm_window", u"Chat", None))
        self.defaultTextInput.setPlaceholderText(QCoreApplication.translate("magi_llm_window", u"Type something here", None))
#if QT_CONFIG(tooltip)
        self.defaultGenerateButton.setToolTip(QCoreApplication.translate("magi_llm_window", u"Send (CTRL+Enter)", None))
#endif // QT_CONFIG(tooltip)
        self.defaultGenerateButton.setText(QCoreApplication.translate("magi_llm_window", u"Generate", None))
#if QT_CONFIG(shortcut)
        self.defaultGenerateButton.setShortcut(QCoreApplication.translate("magi_llm_window", u"Ctrl+Return", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.defaultContinueButton.setToolTip(QCoreApplication.translate("magi_llm_window", u"Continue the last generation", None))
#endif // QT_CONFIG(tooltip)
        self.defaultContinueButton.setText(QCoreApplication.translate("magi_llm_window", u"Continue", None))
#if QT_CONFIG(tooltip)
        self.defaultClearButton.setToolTip(QCoreApplication.translate("magi_llm_window", u"Clear the output", None))
#endif // QT_CONFIG(tooltip)
        self.defaultClearButton.setText(QCoreApplication.translate("magi_llm_window", u"Clear", None))
#if QT_CONFIG(tooltip)
        self.defaultStopButton.setToolTip(QCoreApplication.translate("magi_llm_window", u"Stop generation", None))
#endif // QT_CONFIG(tooltip)
        self.defaultStopButton.setText(QCoreApplication.translate("magi_llm_window", u"Stop", None))
        self.default_modeTextHistory.setPlaceholderText(QCoreApplication.translate("magi_llm_window", u"Output appears here", None))
        self.textgenTab.setTabText(self.textgenTab.indexOf(self.standard_textgenTab), QCoreApplication.translate("magi_llm_window", u"Standard", None))
#if QT_CONFIG(tooltip)
        self.notebookGenerateButton.setToolTip(QCoreApplication.translate("magi_llm_window", u"Send (CTRL+Enter)", None))
#endif // QT_CONFIG(tooltip)
        self.notebookGenerateButton.setText(QCoreApplication.translate("magi_llm_window", u"Generate", None))
#if QT_CONFIG(shortcut)
        self.notebookGenerateButton.setShortcut(QCoreApplication.translate("magi_llm_window", u"Ctrl+Return", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.notebookClearButton.setToolTip(QCoreApplication.translate("magi_llm_window", u"Clear the output", None))
#endif // QT_CONFIG(tooltip)
        self.notebookClearButton.setText(QCoreApplication.translate("magi_llm_window", u"Clear", None))
#if QT_CONFIG(tooltip)
        self.notebookContinueButton.setToolTip(QCoreApplication.translate("magi_llm_window", u"Continue the last generation", None))
#endif // QT_CONFIG(tooltip)
        self.notebookContinueButton.setText(QCoreApplication.translate("magi_llm_window", u"Continue", None))
        self.notebookStopButton.setText(QCoreApplication.translate("magi_llm_window", u"Stop", None))
#if QT_CONFIG(tooltip)
        self.notebook_modeTextHistory.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.notebook_modeTextHistory.setPlaceholderText(QCoreApplication.translate("magi_llm_window", u"Type something here", None))
        self.textgenTab.setTabText(self.textgenTab.indexOf(self.notebook_textgenTab), QCoreApplication.translate("magi_llm_window", u"Notebook", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("magi_llm_window", u"Preferences:", None))
        self.label_28.setText(QCoreApplication.translate("magi_llm_window", u"llama.cpp: Model path:", None))
#if QT_CONFIG(tooltip)
        self.streamEnabledCheck.setToolTip(QCoreApplication.translate("magi_llm_window", u"Stream responses", None))
#endif // QT_CONFIG(tooltip)
        self.streamEnabledCheck.setText(QCoreApplication.translate("magi_llm_window", u"Stream responses", None))
        self.RWKVcppModelSelect.setText(QCoreApplication.translate("magi_llm_window", u"...", None))
        self.label_3.setText(QCoreApplication.translate("magi_llm_window", u"Exllama: Model directory:", None))
#if QT_CONFIG(tooltip)
        self.logChatCheck.setToolTip(QCoreApplication.translate("magi_llm_window", u"Write chat logs to file", None))
#endif // QT_CONFIG(tooltip)
        self.logChatCheck.setText(QCoreApplication.translate("magi_llm_window", u"Log chats", None))
#if QT_CONFIG(tooltip)
        self.rwkvCppModelPath.setToolTip(QCoreApplication.translate("magi_llm_window", u"Path to GGML model for rwkv.cpp", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.exllamaModelSelect.setToolTip(QCoreApplication.translate("magi_llm_window", u"Select Exllama model folder", None))
#endif // QT_CONFIG(tooltip)
        self.exllamaModelSelect.setText(QCoreApplication.translate("magi_llm_window", u"...", None))
#if QT_CONFIG(tooltip)
        self.cppModelPath.setToolTip(QCoreApplication.translate("magi_llm_window", u"Path to GGML model for llama.cpp", None))
#endif // QT_CONFIG(tooltip)
        self.cppModelPath.setText("")
        self.label_2.setText(QCoreApplication.translate("magi_llm_window", u"RWKV.cpp model path:", None))
#if QT_CONFIG(tooltip)
        self.cppModelSelect.setToolTip(QCoreApplication.translate("magi_llm_window", u"Select GGML model", None))
#endif // QT_CONFIG(tooltip)
        self.cppModelSelect.setText(QCoreApplication.translate("magi_llm_window", u"...", None))
#if QT_CONFIG(tooltip)
        self.exllamaModelPath.setToolTip(QCoreApplication.translate("magi_llm_window", u"Path to Exllama GPTQ model folder (mode file, tokenizer.json, config.json)", None))
#endif // QT_CONFIG(tooltip)
        self.exllamaModelPath.setText("")
#if QT_CONFIG(tooltip)
        self.sendStopStringCheck.setToolTip(QCoreApplication.translate("magi_llm_window", u"Send chat user stop string when generating", None))
#endif // QT_CONFIG(tooltip)
        self.sendStopStringCheck.setText(QCoreApplication.translate("magi_llm_window", u"Send chat stop string", None))
#if QT_CONFIG(tooltip)
        self.settingsPathSaveButton.setToolTip(QCoreApplication.translate("magi_llm_window", u"Save settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsPathSaveButton.setText(QCoreApplication.translate("magi_llm_window", u"Save settings", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("magi_llm_window", u"Themes", None))
#if QT_CONFIG(tooltip)
        self.themeDarkCheck.setToolTip(QCoreApplication.translate("magi_llm_window", u"Use a dark theme", None))
#endif // QT_CONFIG(tooltip)
        self.themeDarkCheck.setText(QCoreApplication.translate("magi_llm_window", u"Dark", None))
#if QT_CONFIG(tooltip)
        self.themeLightCheck.setToolTip(QCoreApplication.translate("magi_llm_window", u"Use a light theme", None))
#endif // QT_CONFIG(tooltip)
        self.themeLightCheck.setText(QCoreApplication.translate("magi_llm_window", u"Light", None))
#if QT_CONFIG(tooltip)
        self.themeNativeCheck.setToolTip(QCoreApplication.translate("magi_llm_window", u"Use OS native theme", None))
#endif // QT_CONFIG(tooltip)
        self.themeNativeCheck.setText(QCoreApplication.translate("magi_llm_window", u"Native", None))
        self.backendGroup.setTitle(QCoreApplication.translate("magi_llm_window", u"Backend:", None))
#if QT_CONFIG(tooltip)
        self.loadModelButton.setToolTip(QCoreApplication.translate("magi_llm_window", u"Load the selected backend and model", None))
#endif // QT_CONFIG(tooltip)
        self.loadModelButton.setText(QCoreApplication.translate("magi_llm_window", u"Load backend", None))
#if QT_CONFIG(tooltip)
        self.cppCheck.setToolTip(QCoreApplication.translate("magi_llm_window", u"Use llama.cpp backend", None))
#endif // QT_CONFIG(tooltip)
        self.cppCheck.setText(QCoreApplication.translate("magi_llm_window", u"llama-cpp-python", None))
#if QT_CONFIG(tooltip)
        self.rwkvCppCheck.setToolTip(QCoreApplication.translate("magi_llm_window", u"Use rwkv.cpp backend", None))
#endif // QT_CONFIG(tooltip)
        self.rwkvCppCheck.setText(QCoreApplication.translate("magi_llm_window", u"rwkv.cpp", None))
#if QT_CONFIG(tooltip)
        self.unloadModelButton.setToolTip(QCoreApplication.translate("magi_llm_window", u"Unload the selected backend and model", None))
#endif // QT_CONFIG(tooltip)
        self.unloadModelButton.setText(QCoreApplication.translate("magi_llm_window", u"Unload backend", None))
#if QT_CONFIG(tooltip)
        self.tsServerCheck.setToolTip(QCoreApplication.translate("magi_llm_window", u"Use TextSynth server backend", None))
#endif // QT_CONFIG(tooltip)
        self.tsServerCheck.setText(QCoreApplication.translate("magi_llm_window", u"TextSynth", None))
#if QT_CONFIG(tooltip)
        self.exllamaCheck.setToolTip(QCoreApplication.translate("magi_llm_window", u"Use Exllama backend", None))
#endif // QT_CONFIG(tooltip)
        self.exllamaCheck.setText(QCoreApplication.translate("magi_llm_window", u"Exllama", None))
#if QT_CONFIG(tooltip)
        self.cppServerCheck.setToolTip(QCoreApplication.translate("magi_llm_window", u"Connects to a launched llama.cpp server instead of llama-cpp-python", None))
#endif // QT_CONFIG(tooltip)
        self.cppServerCheck.setText(QCoreApplication.translate("magi_llm_window", u"llama.cpp server", None))
        self.groupBox.setTitle(QCoreApplication.translate("magi_llm_window", u"Chat prefixes:", None))
#if QT_CONFIG(tooltip)
        self.customResponsePrefix.setToolTip(QCoreApplication.translate("magi_llm_window", u"Prefix to apply to prompts", None))
#endif // QT_CONFIG(tooltip)
        self.customResponsePrefix.setText(QCoreApplication.translate("magi_llm_window", u"Sure! ", None))
#if QT_CONFIG(tooltip)
        self.yourNameLine.setToolTip(QCoreApplication.translate("magi_llm_window", u"User name to be used in chat", None))
#endif // QT_CONFIG(tooltip)
        self.yourNameLine.setText(QCoreApplication.translate("magi_llm_window", u"User", None))
#if QT_CONFIG(tooltip)
        self.customResponsePrefixCheck.setToolTip(QCoreApplication.translate("magi_llm_window", u"Apply custom prefix to prompts", None))
#endif // QT_CONFIG(tooltip)
        self.customResponsePrefixCheck.setText(QCoreApplication.translate("magi_llm_window", u"Response prefix:", None))
#if QT_CONFIG(tooltip)
        self.label_4.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("magi_llm_window", u"User name:", None))
#if QT_CONFIG(tooltip)
        self.botNameLine.setToolTip(QCoreApplication.translate("magi_llm_window", u"Bot name to be used in chat", None))
#endif // QT_CONFIG(tooltip)
        self.botNameLine.setText(QCoreApplication.translate("magi_llm_window", u"Assistant", None))
#if QT_CONFIG(tooltip)
        self.label_5.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("magi_llm_window", u"Bot name:", None))
        self.textgenTab.setTabText(self.textgenTab.indexOf(self.settingsTab), QCoreApplication.translate("magi_llm_window", u"Settings", None))
        self.menuFile.setTitle(QCoreApplication.translate("magi_llm_window", u"File", None))
    # retranslateUi

