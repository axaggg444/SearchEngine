import requests
from bs4 import BeautifulSoup
import sqlite3
import threading
import json
import time
import os

try:
    os.remove("database.db")
except:
    pass

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

sql = """
    CREATE TABLE IF NOT EXISTS TBL_Search(
        ID INTEGER PRIMARY KEY,
        url TEXT,
        title TEXT,
        description TEXT,
        author TEXT
    )
"""

cursor.execute(sql)
connection.commit()

def Scrape(url, id):
    try:
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        r = requests.get("https://" + url)

        Soup = BeautifulSoup(r.content, "html.parser")
        title = Soup.find("title")
        title = str(title).replace("<title>", "")
        title = title.replace("</title>", "")

        try:
            description = Soup.find("meta", attrs={"name": "description"})
            description = description["content"]
        except Exception as e:
            description = "NONE"

        try:
            author = Soup.find("meta", attrs={"name": "author"})
            author = author["content"]
        except Exception as e:
            author = "NONE"

        values = (id, url, title, description, author)
        sql = f"""INSERT INTO TBL_Search VALUES (
            ?, ?, ?, ?, ?
        )"""

        cursor.execute(sql, values)
        connection.commit()

    except Exception as e:
        print(f"Failure during Thread {id}.\nHost:{url}")
        print(e)

def GetJson(file, name):
    with open(file, "r") as f:
        data = json.load(f)
        return data[name]

Whitelist = GetJson("Scraper/data/Whitelist.json", "Whitelist")

id = 0
for i in Whitelist:
    ScrapeThread = threading.Thread(target=Scrape, args=(i, id))
    ScrapeThread.daemon = True
    ScrapeThread.start()
    id = id + 1

time.sleep(5)