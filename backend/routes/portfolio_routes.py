from flask import Blueprint, jsonify
from utils.db import get_db

portfolio_bp = Blueprint("portfolio", __name__)

@portfolio_bp.route("/<username>", methods=["GET"])
def get_portfolio(username):
    conn = get_db()
    c = conn.cursor()

    data = c.execute("""
        SELECT p.name, i.shares, p.rent
        FROM investments i
        JOIN properties p ON i.property_id = p.id
        WHERE i.username=?
    """, (username,)).fetchall()

    result = []
    for name, shares, rent in data:
        result.append({
            "name": name,
            "shares": shares,
            "monthly_income": (rent / 100) * shares
        })

    conn.close()
    return jsonify(result)