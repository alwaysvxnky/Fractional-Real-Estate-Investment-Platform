from flask import Blueprint, jsonify
from utils.db import get_db

property_bp = Blueprint("property", __name__)

@property_bp.route("/", methods=["GET"])
def get_properties():
    conn = get_db()
    c = conn.cursor()

    data = c.execute("SELECT * FROM properties").fetchall()

    result = []
    for p in data:
        result.append({
            "id": p[0],
            "name": p[1],
            "location": p[2],
            "price": p[3],
            "total_shares": p[4],
            "available_shares": p[5],
            "rent": p[6]
        })

    conn.close()
    return jsonify(result)