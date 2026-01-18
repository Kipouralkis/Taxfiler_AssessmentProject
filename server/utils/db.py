import os
import sqlite3
from . import init_db

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
DB_PATH = os.path.join(DATA_DIR, "database.db")

# ensure directory exists
os.makedirs(DATA_DIR, exist_ok=True)

# initialize DB once
if not os.path.exists(DB_PATH):
    init_db.initialize_database(DB_PATH)

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn
