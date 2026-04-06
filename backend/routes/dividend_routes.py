from flask import Blueprint, jsonify
from utils.db import get_db

dividend_bp = Blueprint("dividend", __name__)

@dividend_bp.route("/", methods=["GET"])
def get_dividend():
    conn = get_db()
    c = conn.cursor()

    try:
        data = c.execute(
            "SELECT rent, total_shares, available_shares FROM properties"
        ).fetchall()

        total_dividend = 0

        for rent, total_shares, available_shares in data:
            sold_shares = total_shares - available_shares

            if total_shares > 0:
                total_dividend += (rent * sold_shares / total_shares)

        return jsonify({
            "monthly_dividend": round(total_dividend, 2)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        conn.close()