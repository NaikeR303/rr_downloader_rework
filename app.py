import sys
import logging
import os
import time
from enum import Enum, auto
from threading import Thread
from PySide6.QtCore import QTimer, QObject, QSize, Signal
from PySide6.QtWidgets import QApplication, QDialog, QMessageBox, QPushButton

from ui import Ui_Form

from downloader import Downloader
from renderer import Renderer, Styles


class Filetypes(Enum):
    TXT = auto()
    PDF = auto()
    HTML = auto()
    EPUB = auto()

class RoyalRoadDownloader(QDialog, Ui_Form):
    progress_signal = Signal(str, int)
    finish_signal = Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)    

        #Logging
        open('app.log', 'w').close()
        logging.basicConfig(level=logging.INFO, 
                        format='[%(asctime)s | %(levelname)s] %(message)s',
                        handlers=[logging.StreamHandler(),
                                logging.FileHandler(filename='app.log', mode='a')])

        def log_except_hook(excType, excValue, traceback):
            logging.critical("Uncaught exception",
                            exc_info=(excType, excValue, traceback))
        sys.excepthook = log_except_hook

        logging.info("App started!")

        #Variables
        self.book_style = None
        self.book_filetype = None

        #Basic setup
        self.url_box.setText("https://www.royalroad.com/fiction/114710/engineering-magic-and-kitsune")

        self.rr_light_butt.clicked.connect(self.switch_style_buttons)
        self.rr_dark_butt.clicked.connect(self.switch_style_buttons)
        self.midnight_butt.clicked.connect(self.switch_style_buttons)
        self.sepia_butt.clicked.connect(self.switch_style_buttons)

        self.html_butt.clicked.connect(self.switch_filetype_buttons)
        self.pdf_butt.clicked.connect(self.switch_filetype_buttons)
        self.epub_butt.clicked.connect(self.switch_filetype_buttons)

        self.progress_signal.connect(self.update_info)

        self.download_butt.clicked.connect(lambda: Thread(target=self.download).start())

        #Setting first buttons
        self.midnight_butt.click()
        self.html_butt.click()

        self.setFixedSize(QSize(560, 400))

        logging.info("Initialised app!")

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

        #Setting 
        match button:
            case self.rr_light_butt:
                self.book_style = Styles.LIGHT
                logging.info(f"Pressed {Styles.LIGHT} button...")
            case self.rr_dark_butt:
                self.book_style = Styles.DARK
                logging.info(f"Pressed {Styles.DARK} button...")
            case self.midnight_butt:
                self.book_style = Styles.MIDNIGHT
                logging.info(f"Pressed {Styles.MIDNIGHT} button...")
            case self.sepia_butt:
                self.book_style = Styles.SEPIA
                logging.info(f"Pressed {Styles.SEPIA} button...")

    def switch_filetype_buttons(self):
        buttons = [
            self.html_butt,
            self.pdf_butt,
            self.epub_butt,
        ]

        for b in buttons:
            b.setProperty("state", "")

        button = self.sender()

        button.setProperty("state", "selected")

        #Updating buttons
        for b in buttons:
            b.style().polish(b)

        #Setting 
        match button:
            case self.html_butt:
                self.book_filetype = Filetypes.HTML
                logging.info(f"Pressed {Filetypes.HTML} button...")
            case self.pdf_butt:
                self.book_filetype = Filetypes.PDF
                logging.info(f"Pressed {Filetypes.PDF} button...")
            case self.epub_butt:
                self.book_filetype = Filetypes.EPUB
                logging.info(f"Pressed {Filetypes.EPUB} button...")

    def download(self):
        logging.info("Started downloading!")
        logging.info(self.url_box.text())
        
        downloader = Downloader(self.url_box.text())

        url_list = downloader.get_url_list()

        for i, chap in enumerate(url_list):
            downloader.load_chapter(chap)
            self.progress_signal.emit("Loading chapters", (i / len(url_list)) * 90)

        self.progress_signal.emit("Giving chapters", 95)
        
        renderer = Renderer(downloader.get_chapters())

        self.progress_signal.emit("Converting", 99)

        save_path = Renderer._safe_name(downloader.fiction_title)

        match self.book_filetype:
            case Filetypes.HTML:
                renderer.to_html(save_path, self.book_style, downloader.fiction_title, downloader.author_name)
            case Filetypes.PDF:
                renderer.to_pdf(save_path, self.book_style, downloader.fiction_title, downloader.author_name)
            case Filetypes.EPUB:
                renderer.to_epub(save_path, downloader.fiction_title, downloader.author_name)

        self.progress_signal.emit("DONE!", 100)


    def update_info(self, message, number):
        self.progressBar.setValue(number)
        self.progressBar.setFormat(f"{message} - %p%")
#Main
app = QApplication(sys.argv)

window = RoyalRoadDownloader()
window.show()

sys.exit(app.exec())