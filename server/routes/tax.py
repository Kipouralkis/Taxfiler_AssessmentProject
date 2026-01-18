from flask import Blueprint, render_template, request, flash, abort
from services.tax_service import process_tax_submission

tax_bp = Blueprint("tax", __name__)

@tax_bp.route("/")
def index():
    return render_template("index.html", app_name="EasyTax!")

@tax_bp.route("/create", methods=["POST"])
def create():
    result = process_tax_submission(request.form)

    if result["status"] == "error":
        for msg in result["messages"]:
            flash(msg, "error")
        return render_template("index.html", app_name="EasyTax!", form_data=result["data"])

    # success → show advice
    return render_template("index.html", app_name="EasyTax!", advice=result["advice"])
