from flask import Blueprint, request, jsonify

ml_bp = Blueprint("ml", __name__)

@ml_bp.route("/predict", methods=["POST"])
def predict():
    data = request.json
    price = data["price"]
    rent = data["rent"]

    roi = (rent * 12 / price) * 100
    return jsonify({"roi": round(roi, 2)})