from utils.db import get_db_connection

def insert_tax_record(data):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO taxInfo (income, expenses, filing_status, dependents, investment_assets) VALUES (?, ?, ?, ?, ?)",
        [
            data["income"],
            data["expenses"],
            data["filing_status"],
            data["dependents"],
            data["investment_assets"]
        ]
    )

    conn.commit()
    conn.close()
