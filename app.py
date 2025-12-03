import sys
import logging
import os
from threading import Thread
from PySide6.QtCore import QTimer, QObject, QSize, Signal
from PySide6.QtWidgets import QApplication, QDialog, QMessageBox, QPushButton
from downloader import Downloader
from ui import Ui_Form

class Styles:
    light = 1
    dark = 2
    midnight = 3
    sepia = 4

class Filetypes:
    txt = 1
    pdf = 2
    html = 3
    epub = 4

class RoyalRoadDownloader(QDialog, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)    

        #Logging
        def log_except_hook(excType, excValue, traceback):
            logging.critical("Uncaught exception",
                            exc_info=(excType, excValue, traceback))
        sys.excepthook = log_except_hook

        #Variables
        self.book_style = None

        #Basic setup
        self.url_box.setText("https://www.royalroad.com/fiction/114710/engineering-magic-and-kitsune")

        self.rr_light_butt.clicked.connect(self.switch_style_buttons)
        self.rr_dark_butt.clicked.connect(self.switch_style_buttons)
        self.midnight_butt.clicked.connect(self.switch_style_buttons)
        self.sepia_butt.clicked.connect(self.switch_style_buttons)

        

        #Setting first buttons
        self.midnight_butt.click()

        self.setFixedSize(QSize(560, 400))

    def switch_style_buttons(self):
        buttons = [
            self.rr_light_butt,
            self.rr_dark_butt,
            self.midnight_butt,
            self.sepia_butt
        ]

        for b in buttons:
            b.setProperty("state", "")

        button = self.sender()

        button.setProperty("state", "selected")

        #Updating buttons
        for b in buttons:
            b.style().polish(b)


        # match button:
        #     case self.rr_light_butt:
        #         print("hello")
        #     case self.rr_dark_butt:
        #         print("world")
        #     case self.midnight_butt:
        #         print("!!!")
        #     case self.sepia_butt:
        #         print("!!")

#Main
app = QApplication(sys.argv)

window = RoyalRoadDownloader()
window.show()

sys.exit(app.exec())