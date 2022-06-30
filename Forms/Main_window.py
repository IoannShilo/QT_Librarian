# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(950, 650)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(950, 650))
        MainWindow.setMaximumSize(QSize(950, 650))
        self.actionLog_in = QAction(MainWindow)
        self.actionLog_in.setObjectName(u"actionLog_in")
        self.actionLog_out = QAction(MainWindow)
        self.actionLog_out.setObjectName(u"actionLog_out")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_7 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QSize(540, 400))
        self.groupBox.setMaximumSize(QSize(540, 400))
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetFixedSize)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QSize(180, 90))
        self.pushButton.setMaximumSize(QSize(180, 90))

        self.horizontalLayout.addWidget(self.pushButton)

        self.verticalSpacer = QSpacerItem(50, 80, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.horizontalLayout.addItem(self.verticalSpacer)

        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QSize(180, 90))
        self.pushButton_2.setMaximumSize(QSize(180, 90))

        self.horizontalLayout.addWidget(self.pushButton_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalSpacer_2 = QSpacerItem(18, 90, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.horizontalLayout_2.addItem(self.verticalSpacer_2)

        self.pushButton_3 = QPushButton(self.groupBox)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QSize(180, 90))
        self.pushButton_3.setMaximumSize(QSize(180, 90))

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.verticalSpacer_3 = QSpacerItem(20, 90, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.horizontalLayout_2.addItem(self.verticalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_6 = QPushButton(self.groupBox)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setMinimumSize(QSize(180, 90))
        self.pushButton_6.setMaximumSize(QSize(180, 90))

        self.horizontalLayout_3.addWidget(self.pushButton_6)

        self.verticalSpacer_4 = QSpacerItem(50, 90, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.horizontalLayout_3.addItem(self.verticalSpacer_4)

        self.pushButton_5 = QPushButton(self.groupBox)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMinimumSize(QSize(180, 90))
        self.pushButton_5.setMaximumSize(QSize(180, 90))

        self.horizontalLayout_3.addWidget(self.pushButton_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_5.addWidget(self.groupBox)

        self.horizontalSpacer_5 = QSpacerItem(40, 100, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_5.addItem(self.horizontalSpacer_5)


        self.horizontalLayout_5.addLayout(self.verticalLayout_5)

        self.verticalSpacer_5 = QSpacerItem(30, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_5.addItem(self.verticalSpacer_5)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QSize(360, 500))
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.calendarWidget = QCalendarWidget(self.groupBox_2)
        self.calendarWidget.setObjectName(u"calendarWidget")

        self.verticalLayout_4.addWidget(self.calendarWidget)

        self.horizontalSpacer_3 = QSpacerItem(40, 50, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_4.addItem(self.horizontalSpacer_3)

        self.lcdNumber = QLCDNumber(self.groupBox_2)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setMinimumSize(QSize(250, 80))

        self.verticalLayout_4.addWidget(self.lcdNumber)

        self.horizontalSpacer_4 = QSpacerItem(40, 50, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_4.addItem(self.horizontalSpacer_4)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_4.addItem(self.verticalSpacer_6)

        self.pushButton_4 = QPushButton(self.groupBox_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(150, 80))

        self.horizontalLayout_4.addWidget(self.pushButton_4)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_4.addItem(self.verticalSpacer_7)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)


        self.horizontalLayout_5.addWidget(self.groupBox_2)


        self.verticalLayout_7.addLayout(self.horizontalLayout_5)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 950, 21))
        self.menubar.setNativeMenuBar(True)
        self.menudddd = QMenu(self.menubar)
        self.menudddd.setObjectName(u"menudddd")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menudddd.menuAction())
        self.menudddd.addAction(self.actionLog_in)
        self.menudddd.addAction(self.actionLog_out)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionLog_in.setText(QCoreApplication.translate("MainWindow", u"Log in", None))
        self.actionLog_out.setText(QCoreApplication.translate("MainWindow", u"Log out", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Working with readers", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Readers", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Young\n"
"readers", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Register\n"
"a new reader", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Booking of\n"
"books", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Lending of\n"
"books", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Information", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Book\n"
"search", None))
        self.menudddd.setTitle(QCoreApplication.translate("MainWindow", u"Database", None))
    # retranslateUi

