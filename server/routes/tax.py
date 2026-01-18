from flask import Blueprint, request, jsonify
from services.tax_service import process_tax_submission

tax_bp = Blueprint("tax", __name__)

@tax_bp.route("/")
def index():
    return jsonify({"message": "Taxfiler API is running"})


@tax_bp.route("/api/tax", methods=["POST"])
def create_tax():
    data = request.json
    result = process_tax_submission(data)
    return jsonify(result)
