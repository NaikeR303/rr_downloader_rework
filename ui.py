# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainnhTVTA.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QProgressBar, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(560, 400)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet(u"background-color: black;\n"
"font-family: Monospace;")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QWidget{\n"
"	background-color: #171717;\n"
"}\n"
"\n"
"QFrame{\n"
"	border-radius: 16px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: red;\n"
"	padding: 5px 5px;\n"
"    font-size: 16px;\n"
"    border-radius: 12px;\n"
"\n"
"	border: 0px solid rgb(255, 120, 0);\n"
"}\n"
"\n"
"QPushButton[state=\"selected\"]{\n"
"	border:  2px solid rgb(255, 120, 0);\n"
"}\n"
"QPushButton[state=\"\"]{\n"
"	border:  0px solid rgb(255, 120, 0);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 20))
        font = QFont()
        font.setFamilies([u"Monospace"])
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.url_box = QLineEdit(self.frame)
        self.url_box.setObjectName(u"url_box")
        self.url_box.setStyleSheet(u"background-color: grey;")

        self.verticalLayout.addWidget(self.url_box)

        self.frame1 = QFrame(self.frame)
        self.frame1.setObjectName(u"frame1")
        font1 = QFont()
        font1.setFamilies([u"Monospace"])
        font1.setKerning(True)
        self.frame1.setFont(font1)
        self.frame1.setStyleSheet(u"")
        self.frame1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame1)
        self.horizontalLayout.setSpacing(9)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 9, 0, 0)
        self.frame_2 = QFrame(self.frame1)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QWidget{\n"
"	background-color: #282828;\n"
"}\n"
"")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 20))
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_3)

        self.rr_light_butt = QPushButton(self.frame_2)
        self.rr_light_butt.setObjectName(u"rr_light_butt")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.rr_light_butt.sizePolicy().hasHeightForWidth())
        self.rr_light_butt.setSizePolicy(sizePolicy1)
        self.rr_light_butt.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    color: black;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #CACACA;\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color: #3D3730;\n"
"}")

        self.verticalLayout_2.addWidget(self.rr_light_butt)

        self.rr_dark_butt = QPushButton(self.frame_2)
        self.rr_dark_butt.setObjectName(u"rr_dark_butt")
        sizePolicy1.setHeightForWidth(self.rr_dark_butt.sizePolicy().hasHeightForWidth())
        self.rr_dark_butt.setSizePolicy(sizePolicy1)
        self.rr_dark_butt.setStyleSheet(u"QPushButton {\n"
"    background-color: #131313;\n"
"    color: #CFCFCF;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #2D2D2D;\n"
"}\n"
"QPushButton:disable {\n"
"    background-color: #3D3730;\n"
"}")

        self.verticalLayout_2.addWidget(self.rr_dark_butt)

        self.midnight_butt = QPushButton(self.frame_2)
        self.midnight_butt.setObjectName(u"midnight_butt")
        sizePolicy1.setHeightForWidth(self.midnight_butt.sizePolicy().hasHeightForWidth())
        self.midnight_butt.setSizePolicy(sizePolicy1)
        self.midnight_butt.setStyleSheet(u"QPushButton {\n"
"    background-color: #1A1A1A;\n"
"    color: #808080;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #333333;\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color: #3D3730;\n"
"}")

        self.verticalLayout_2.addWidget(self.midnight_butt)

        self.sepia_butt = QPushButton(self.frame_2)
        self.sepia_butt.setObjectName(u"sepia_butt")
        sizePolicy1.setHeightForWidth(self.sepia_butt.sizePolicy().hasHeightForWidth())
        self.sepia_butt.setSizePolicy(sizePolicy1)
        self.sepia_butt.setStyleSheet(u"QPushButton {\n"
"    background-color: #af926d;\n"
"    color: #52331e;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #715C42;\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color: #3D3730;\n"
"}")

        self.verticalLayout_2.addWidget(self.sepia_butt)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame1)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QWidget{\n"
"	background-color: #282828;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #8D8D8D;\n"
"    color: black;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #6C6C6C;\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color: #363636;\n"
"}")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 20))
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_4)

        self.html_butt = QPushButton(self.frame_3)
        self.html_butt.setObjectName(u"html_butt")
        sizePolicy1.setHeightForWidth(self.html_butt.sizePolicy().hasHeightForWidth())
        self.html_butt.setSizePolicy(sizePolicy1)
        self.html_butt.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.html_butt)

        self.pdf_butt = QPushButton(self.frame_3)
        self.pdf_butt.setObjectName(u"pdf_butt")
        sizePolicy1.setHeightForWidth(self.pdf_butt.sizePolicy().hasHeightForWidth())
        self.pdf_butt.setSizePolicy(sizePolicy1)
        self.pdf_butt.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.pdf_butt)

        self.epub_butt = QPushButton(self.frame_3)
        self.epub_butt.setObjectName(u"epub_butt")
        sizePolicy1.setHeightForWidth(self.epub_butt.sizePolicy().hasHeightForWidth())
        self.epub_butt.setSizePolicy(sizePolicy1)
        self.epub_butt.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.epub_butt)


        self.horizontalLayout.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame1)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QWidget{\n"
"	background-color: #282828;\n"
"}\n"
"")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.download_butt = QPushButton(self.frame_4)
        self.download_butt.setObjectName(u"download_butt")
        sizePolicy1.setHeightForWidth(self.download_butt.sizePolicy().hasHeightForWidth())
        self.download_butt.setSizePolicy(sizePolicy1)
        self.download_butt.setStyleSheet(u"QPushButton{\n"
"	background-color: #f15e2a;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #f1412a;\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.download_butt)

        self.progressBar = QProgressBar(self.frame_4)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.verticalLayout_4.addWidget(self.progressBar)


        self.verticalLayout.addWidget(self.frame_4)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"PUT LINK HERE", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"CHOOSE YOUR STYLE", None))
        self.rr_light_butt.setText(QCoreApplication.translate("Form", u"RR LIGHT", None))
        self.rr_dark_butt.setText(QCoreApplication.translate("Form", u"RR DARK", None))
        self.midnight_butt.setText(QCoreApplication.translate("Form", u"MIDNIGHT", None))
        self.sepia_butt.setText(QCoreApplication.translate("Form", u"SEPIA", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"CHOOSE FORMAT", None))
        self.html_butt.setText(QCoreApplication.translate("Form", u"HTML", None))
        self.pdf_butt.setText(QCoreApplication.translate("Form", u"PDF", None))
        self.epub_butt.setText(QCoreApplication.translate("Form", u"EPUB", None))
        self.download_butt.setText(QCoreApplication.translate("Form", u"DOWNLOAD", None))
    # retranslateUi

