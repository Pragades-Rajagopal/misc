import sqlite3

conn = sqlite3.connect('database.db')

with open('schema.sql') as foo:
    conn.executescript(foo.read())

cur = conn.cursor()

cur.execute("INSERT INTO posts (title, content, created, priority) values(?,?,?,?)",
('First Release', 'This is the first public release of note taking application', '2021/10/30 11:00:00', 'P2'))


conn.commit()
conn.close()

