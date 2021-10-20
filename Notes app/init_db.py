import sqlite3

conn = sqlite3.connect('database.db')

with open('schema.sql') as foo:
    conn.executescript(foo.read())

cur = conn.cursor()

cur.execute("INSERT INTO posts (title, content) values(?,?)",
('First Release', 'This is the first public release of note taking application'))

cur.execute("INSERT INTO posts (title, content) values(?,?)",
('Bug squashes', 'Check for any bugs and fix them! Timestamp is now changed to localtime'))

cur.execute("INSERT INTO posts (title, content) values(?,?)",
('Enhancements!', 'Bring new ideas and enhancements to the existing application'))

cur.execute("INSERT INTO posts (title, content) values(?,?)",
('Celebration time mates!', 'Hurray!!! It''s time to celebrate for the launch of our first application!'))

conn.commit()
conn.close()

