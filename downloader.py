import sqlite3
import hashlib
import requests
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

class IncorrectURLError (Exception):
    def __init__(self):
        super().__init__("Incorrect URL was given, check if it fits template")


class Downloader:
    """Give it URL from RR and it'll give you all content
    
    URL template: https://www.royalroad.com/fiction/{id}"""
    def __init__(self, raw_url:str):
        # Init DB
        db_name = "chapter_db.db"

        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

        # Create tables
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
                content     TEXT,     

                FOREIGN KEY (fiction_id) REFERENCES fictions(fiction_id) ON DELETE CASCADE       
            )
            '''
        )

        # Checking if URL is correct and getting fiction ID
        try:
            self.fiction_id  = raw_url.split("/")[4]

            self.fiction_url = f"https://www.royalroad.com/fiction/{self.fiction_id}"

            if not self.fiction_id.isnumeric():
                raise IncorrectURLError
            
            self.fiction_id = int(self.fiction_id)
        except IndexError:
            raise IncorrectURLError
        
        soup = BeautifulSoup(requests.get(self.fiction_url).content, "html.parser")

        # Getting info
        self.author_name = soup.find("div", class_="portlet-body").find("a").text
        self.title = soup.find("div", class_="fic-header").find("h1").text

        # Writing to DB
        self.cursor.execute(
            """
            INSERT OR REPLACE INTO fictions (fiction_id, url, title, author) VALUES (?, ?, ?, ?)
            """,
            (self.fiction_id, self.fiction_url, self.title, self.author_name)
        )

        # Committing changes
        self.conn.commit()


    def _get_url_list(self):
        soup = BeautifulSoup(requests.get(f"https://www.royalroad.com/fiction/{self.fiction_id}").content, "html.parser")

        lis = soup.find("tbody")
        lis = lis.find_all("tr")

        print(lis)


if __name__ == "__main__":
    d = Downloader("https://www.royalroad.com/fiction/114710/engineering-magic-and-kitsune")

    # d._get_url_list()