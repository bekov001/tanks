import sqlite3

con = sqlite3.connect("data.db")
cur = con.cursor()

cur.execute("""CREATE TABLE music (
    ID   INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME STRING,
    SONG BLOB
);
""")
con.commit()
cur.execute("""
CREATE TABLE image (
    ID   INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME STRING,
    IMG  BLOB
);
""")

con.commit()