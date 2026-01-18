from utils.validations import sanitize_input, validate_input
from services.db_service import insert_tax_record
from services.ai_service import generate_advice

def process_tax_submission(form):
    data = {
        "income": form.get("income"),
        "expenses": form.get("expenses"),
        "filing_status": form.get("filing-status"),
        "dependents": form.get("dependents"),
        "investment_assets": form.get("investment-assets")
    }

    # missing fields
    missing = [k for k, v in data.items() if not v]
    if missing:
        return {
            "status": "error",
            "messages": [f"Missing required fields: {', '.join(missing)}"],
            "data": data
        }

    sanitized = sanitize_input(data)
    errors = validate_input(sanitized)

    if errors:
        return {
            "status": "error",
            "messages": list(errors.values()),
            "data": data
        }

    insert_tax_record(sanitized)
    advice = generate_advice(sanitized)

    return {
        "status": "success",
        "advice": advice
    }
