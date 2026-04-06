from flask import Blueprint, request, jsonify
from utils.db import get_db

investment_bp = Blueprint("investment", __name__)

@investment_bp.route("/buy", methods=["POST"])
def buy_shares():
    data = request.json
    property_id = data["property_id"]
    shares = data["shares"]
    username = data["username"]

    conn = get_db()
    c = conn.cursor()

    prop = c.execute(
        "SELECT * FROM properties WHERE id=?",
        (property_id,)
    ).fetchone()

    if not prop:
        return jsonify({"msg": "Property not found"}), 404

    if prop[5] < shares:
        return jsonify({"msg": "Not enough shares"}), 400

    # Update property shares
    c.execute(
        "UPDATE properties SET available_shares = available_shares - ? WHERE id=?",
        (shares, property_id)
    )

    # Add to user portfolio
    existing = c.execute(
        "SELECT * FROM investments WHERE username=? AND property_id=?",
        (username, property_id)
    ).fetchone()

    if existing:
        c.execute(
            "UPDATE investments SET shares = shares + ? WHERE id=?",
            (shares, existing[0])
        )
    else:
        c.execute(
            "INSERT INTO investments (username, property_id, shares) VALUES (?, ?, ?)",
            (username, property_id, shares)
        )

    conn.commit()
    conn.close()

    return jsonify({"msg": "Purchased"})