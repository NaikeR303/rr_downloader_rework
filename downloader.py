import sqlite3
import pathlib
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

        #Checking if table exists
        req = self.conn.execute(
            "SELECT 1 FROM sqlite_master WHERE type='table' AND name='chapters'"
        )
        table_exists = req.fetchone() is not None

        if not table_exists:
            logging.warning("DB doesn't exist!")

            # Create tables
            logging.info("Setting tables for DB...")
            # For foreign keys
            self.conn.execute("PRAGMA foreign_keys = ON")

            self.conn.execute(
                '''
                CREATE TABLE fictions (
                    fiction_id  TEXT PRIMARY KEY,  
                    url         TEXT UNIQUE,
                    cover       TEXT,
                    title       TEXT NOT NULL,
                    author      TEXT
                )
                '''
            )
            
            self.conn.execute(
                '''            
                CREATE TABLE chapters (
                    chapter_id  TEXT PRIMARY KEY,  
                    fiction_id  TEXT NOT NULL,  
                    url         TEXT UNIQUE,              
                    date        TEXT,              
                    title       TEXT,     
                    content     TEXT,     

                    FOREIGN KEY (fiction_id) REFERENCES fictions(fiction_id) ON DELETE CASCADE       
                )
                '''
            )
            self.conn.commit()

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

        logging.info("Writing fiction info to DB...")
        # Writing to DB
        self.conn.execute(
            """
            INSERT OR REPLACE INTO fictions (fiction_id, url, title, author) VALUES (?, ?, ?, ?)
            """,
            (self.fiction_id, self.fiction_url, self.fiction_title, self.author_name)
        )

        # Committing changes
        self.conn.commit()


    def get_url_list(self, id_only = True):
        logging.info("Collecting chapter URLs...")
        logging.info(f"Only ID = {id_only}")

        soup = BeautifulSoup(requests.get(f"https://www.royalroad.com/fiction/{self.fiction_id}").content, "html.parser")

        chapter_list = [chap.find("a")['href'] for chap in soup.find("tbody").find_all("tr")]

        if not id_only:
            return chapter_list
        else:
            return [chap.split("/")[5] for chap in chapter_list]

    def load_chapter(self, chapter_id, skip_span = True):
        logging.info(f"Getting chapter with ID {chapter_id}...")

        req = self.conn.execute(
            f"""
            SELECT *
            FROM chapters 
            WHERE chapter_id = ?
            """,
            (chapter_id, )
        )

        if req.fetchone() == None:
            logging.warning("Chapter is not in DB!")

            chapter_url = self.fiction_url + f"/chapter/{chapter_id}"
            # Trying 4 times
            for _ in range(4):
                try: 
                    soup = BeautifulSoup(requests.get(chapter_url).content, features="html.parser")
                    break
                except:
                    pass
            
            content = soup.find("div", class_="chapter-content")

            if skip_span:
                # Removing "Hey, that's not RoyalRoad!"
                logging.info("Removing anti-piracy spans...")
                for span in content.find_all("span", recursive=False):
                    span.decompose()

            release_date = soup.find("time")["datetime"][0:10]
            title = soup.find("h1").text
            
            # Writing to DB
            logging.info("Writing chapter to DB...")

            self.cursor.execute(
                """
                INSERT OR REPLACE INTO chapters (chapter_id, fiction_id, url, date, title, content) VALUES (?, ?, ?, ?, ?, ?)
                """,
                (chapter_id, self.fiction_id, chapter_url, release_date, title, str(content))
            ) 

            self.conn.commit()

        else:
            logging.info("Chapter is already in DB...")

    def get_chapters(self):
        req = self.conn.execute(
            f"""
            SELECT *
            FROM chapters 
            WHERE fiction_id = ?
            """,
            (self.fiction_id, )
        )

        return req.fetchall()


if __name__ == "__main__":

    open('app.log', 'w').close()
    logging.basicConfig(level=logging.INFO, 
                    format='[%(asctime)s | %(levelname)s] %(message)s',
                    handlers=[logging.StreamHandler(),
                            logging.FileHandler(filename='app.log', mode='a')])


    d = Downloader("https://www.royalroad.com/fiction/124235/die-trying-a-roguelite-extraction-litrpg/chapter/2424538/chapter-1")

    print(d.get_url_list())

    for chap in d.get_url_list():
        d.load_chapter(chap)

