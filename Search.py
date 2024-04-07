import re
import sqlite3

def Search(search):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    results = []

    sql = """SELECT * FROM TBL_Search"""
    cursor.execute(sql)

    for dsatz in cursor:
        for i in range(5):
            erg = re.findall(search, str(dsatz[i]))
            if len(erg) != 0 and dsatz[0] not in results:
                results.append(dsatz[0])
            for i in  results:
                for i in range(5):
                    if i == "NONE":
                        results.remove(i)

    connection.close()

    return results