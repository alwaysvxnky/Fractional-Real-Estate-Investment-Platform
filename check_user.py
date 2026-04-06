import sqlite3

conn = sqlite3.connect("backend/database/realestate.db")
c = conn.cursor()

users = c.execute("SELECT * FROM users").fetchall()

print("USERS:", users)

conn.close()