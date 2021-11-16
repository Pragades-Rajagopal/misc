import sqlite3

conn = sqlite3.connect('database.db')

with open('schema.sql') as foo:
    conn.executescript(foo.read())

cur = conn.cursor()

cur.execute("INSERT INTO posts (title, content, created, priority) values(?,?,?,?)",
('First Note', 'First note', '2021/11/16 00:00:00', 'P2'))


conn.commit()
conn.close()

