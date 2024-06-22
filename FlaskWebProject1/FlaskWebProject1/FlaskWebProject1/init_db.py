import sqlite3

connection = sqlite3.connect("database.db")


with open("schema.sql") as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute(
    "INSERT INTO posts (title, content, auctor) VALUES (?, ?, ?)",
    ("test", "test", "test"),
)

cur.execute(
    "INSERT INTO posts (title, content, auctor) VALUES (?, ?, ?)",
    ("test", "test", "auctor"),
)

connection.commit()
connection.close()
