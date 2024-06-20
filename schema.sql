
CREATE TABLE IF NOT EXISTS taxInfo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    income TEXT NOT NULL,
    expenses TEXT NOT NULL,
    filing_status TEXT NOT NULL,
    dependents INTEGER NOT NULL,
    investment_assets TEXT
);