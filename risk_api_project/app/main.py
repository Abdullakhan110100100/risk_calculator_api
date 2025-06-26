from flask import Blueprint, request, jsonify
from app.risk_logic import calculate_risk
from app.auth import token_required

bp = Blueprint('main', __name__)

@bp.route('/api/v1/risk-score', methods=['POST'])
@token_required
def risk_score():
    try:
        data = request.get_json()
        required_fields = ["purpose", "data_sensitivity", "region", "processor_name"]
        if not all(field in data for field in required_fields):
            return jsonify({"error": "Missing required fields"}), 400

        score, breakdown = calculate_risk(data)
        return jsonify({
            "risk_score": score,
            "risk_breakdown": breakdown
        })
    except Exception as e:
        return jsonify({"error": "Internal Server Error"}), 500
