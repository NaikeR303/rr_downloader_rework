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
    def __init__(self, url:str):
        # Init DB
        db_name = "chapter_db.db"

        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

        # Create tables
        # For foreing keys
        self.cursor.execute("PRAGMA foreign_keys = ON")

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS fictions (
                fiction_id INTEGER PRIMARY KEY,  
                url TEXT NOT NULL,
                cover TEXT NOT NULL,
                title TEXT NOT NULL       
            )
            ''')
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS chapters (
                chapter_id INTEGER PRIMARY KEY,  
                fiction_id INTEGER NOT NULL,  
                url TEXT UNIQUE,              
                date TEXT,                   
                content TEXT,               
                FOREIGN KEY (fiction_id) REFERENCES fictions(fiction_id)
                    ON DELETE CASCADE       
            )
            ''')

        self.conn.commit()

        # Getting fiction ID
        try:
            self.fiction_id  = url.split("/")[4]

            if not self.fiction_id.isnumeric():
                raise IncorrectURLError
            
            self.fiction_id = int(self.fiction_id)
        except IndexError:
            raise IncorrectURLError
        
    def _get_url_list(self):
        soup = BeautifulSoup(requests.get(f"https://www.royalroad.com/fiction/{self.fiction_id}").content, "html.parser")

        lis = soup.find("tbody")
        lis = lis.find_all("tr")

        print(lis)


if __name__ == "__main__":
    d = Downloader("https://www.royalroad.com/fiction/139212/the-hundred-reigns-timeloop-litrpg")

    d._get_url_list()