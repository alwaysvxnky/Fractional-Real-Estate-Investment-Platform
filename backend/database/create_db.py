import sqlite3

conn = sqlite3.connect("realestate.db")
c = conn.cursor()

# Create table
c.execute("""
CREATE TABLE IF NOT EXISTS properties(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    location TEXT,
    price REAL,
    total_shares INTEGER,
    available_shares INTEGER,
    rent REAL
)
""")

# Insert sample data
c.execute("""
INSERT INTO properties (name, location, price, total_shares, available_shares, rent)
VALUES (?, ?, ?, ?, ?, ?)
""", ("Luxury Villa", "Chennai", 5000000, 100, 100, 50000))

conn.commit()
conn.close()

print("Database Ready ✅")