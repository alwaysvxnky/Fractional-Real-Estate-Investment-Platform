from utils.db import get_db

def get_all_properties():
    conn = get_db()
    c = conn.cursor()
    return c.execute("SELECT * FROM properties").fetchall()