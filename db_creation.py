import sqlite3
db = sqlite3.connect('funny_word.db')
cur = db.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS User (
    id INT PRIMARY KEY,
    birth INT,
    gender TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS Responses (
    id INT PRIMARY KEY,
    understand INT,
    funny INT,
    frequent INT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS Questions (
    question_id INT PRIMARY KEY,
    question TEXT
)
""")
db.commit()

cur.execute("""
INSERT INTO Questions (question_id, question) VALUES (1, "Насколько оно понятное.")
""")
db.commit()
cur.execute("""
INSERT INTO Questions (question_id, question) VALUES (2, "Насколько оно смешное.")
""")
db.commit()
cur.execute("""
INSERT INTO Questions (question_id, question) VALUES (3, "Насколько часто его используют.")
""")

db.commit()