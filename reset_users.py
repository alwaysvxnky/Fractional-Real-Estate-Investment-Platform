import sqlite3

conn = sqlite3.connect("backend/database/realestate.db")
c = conn.cursor()

c.execute("DELETE FROM users")

conn.commit()
conn.close()

print("✅ All users deleted")