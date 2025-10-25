#! usr/bin/env python3

import sqlite3

conn=sqlite3.connect(':memory:')

cursor=conn.cursor()

cursor.execute("""

CREATE TABLE IF NOT EXISTS books(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL)

    """)

cursor.execute("""
INSERT INTO books (title, author)
VALUES ("LIBRO 1", "AUTOR 1")
""")

cursor.execute("""
INSERT INTO books (title, author)
VALUES ("LIBRO 2", "AUTOR 2")
""")

cursor.execute("""
INSERT INTO books (title, author)
VALUES ("LIBRO 3", "AUTOR 3")
""")

cursor.execute("""
SELECT * FROM books
""")
rows=cursor.fetchall()

for row in rows:
    print(row)

conn.close()

#EOF
