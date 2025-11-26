import sqlite3
import hashlib
import requests
import logging
import sys
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

class IncorrectURLError (Exception):
    def __init__(self):
        super().__init__("Incorrect URL was given, check if it fits template")


class Downloader:
    """Give it URL from RR and it'll give you all content
    
    URL template: https://www.royalroad.com/fiction/{id}"""
    def __init__(self, raw_url:str):
        # Init logging
        def log_except_hook(excType, excValue, traceback):
            logging.critical("Uncaught exception",
                            exc_info=(excType, excValue, traceback))
        sys.excepthook = log_except_hook


        # Init DB
        logging.info("Creating and initiating DB...")

        db_name = "chapter_db.db"

        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

        # Create tables
        logging.info("Setting tables for DB...")
        # For foreign keys
        self.cursor.execute("PRAGMA foreign_keys = ON")

        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS fictions (
                fiction_id  INTEGER PRIMARY KEY,  
                url         TEXT UNIQUE,
                cover       TEXT,
                title       TEXT NOT NULL,
                author      TEXT
            )
            '''
        )
        
        self.cursor.execute(
            '''            
            CREATE TABLE IF NOT EXISTS chapters (
                chapter_id  INTEGER PRIMARY KEY,  
                fiction_id  INTEGER NOT NULL,  
                url         TEXT UNIQUE,              
                date        TEXT,              
                title,      TEXT,     
                content     TEXT,     

                FOREIGN KEY (fiction_id) REFERENCES fictions(fiction_id) ON DELETE CASCADE       
            )
            '''
        )

        # Checking if URL is correct and getting fiction ID
        logging.info("Checking if given URL is correct...")
        try:
            self.fiction_id  = raw_url.split("/")[4]

            self.fiction_url = f"https://www.royalroad.com/fiction/{self.fiction_id}"

            if not self.fiction_id.isnumeric():
                raise IncorrectURLError
            
            self.fiction_id = int(self.fiction_id)
        except IndexError:
            raise IncorrectURLError
        
        logging.info("...it is")

        soup = BeautifulSoup(requests.get(self.fiction_url).content, "html.parser")

        # Getting info
        self.author_name = soup.find("div", class_="portlet-body").find("a").text
        self.fiction_title = soup.find("div", class_="fic-header").find("h1").text

        logging.info("Writing to DB...")
        # Writing to DB
        self.cursor.execute(
            """
            INSERT OR REPLACE INTO fictions (fiction_id, url, title, author) VALUES (?, ?, ?, ?)
            """,
            (self.fiction_id, self.fiction_url, self.fiction_title, self.author_name)
        )

        # Committing changes
        self.conn.commit()


    def _get_url_list(self, id_only = True):
        logging.info("Collecting chapter URLs...")
        logging.info(f"Only ID = {id_only}")

        soup = BeautifulSoup(requests.get(f"https://www.royalroad.com/fiction/{self.fiction_id}").content, "html.parser")

        chapter_list = [chap.find("a")['href'] for chap in soup.find("tbody").find_all("tr")]

        if not id_only:
            return chapter_list
        else:
            return [chap.split("/")[5] for chap in chapter_list]

    def get_chapter(self, chapter_id, skip_span = True):
        logging.info(f"Getting chapter with ID {chapter_id}...")

        self.cursor.execute(
            """
            SELECT 1 FROM chapters WHERE chapter_id = ?
            """,
            (chapter_id)
        )
        if self.cursor.fetchone() == None:
            logging.warning("Chapter is not in DB!")

            chap_url = self.fiction_url + f"/chapter/{chapter_id}"
            for _ in range(4):
                try: 
                    soup = BeautifulSoup(requests.get(chap_url).content)
                    break
                except:
                    pass
            
            content = soup.find("div", class_="chapter-content")

            for span in content.find_all("span"):
                span.decompose()
        else:
            logging.info("Chapter is in DB, getting it...")



if __name__ == "__main__":

    open('app.log', 'w').close()
    logging.basicConfig(level=logging.INFO, 
                    format='[%(asctime)s | %(levelname)s] %(message)s',
                    handlers=[logging.StreamHandler(),
                            logging.FileHandler(filename='app.log', mode='a')])


    d = Downloader("https://www.royalroad.com/fiction/114710/engineering-magic-and-kitsune")

    print(d._get_url_list())