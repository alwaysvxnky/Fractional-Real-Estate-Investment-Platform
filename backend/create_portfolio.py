import sqlite3

# ✅ correct relative path
conn = sqlite3.connect("database/realestate.db")

c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS investments(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    property_id INTEGER,
    shares INTEGER
)
""")

conn.commit()
conn.close()

print("✅ Portfolio table created")