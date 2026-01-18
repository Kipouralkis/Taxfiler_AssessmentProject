import sqlite3

def initialize_database(db_path):
    try:
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        # Read schema.sql and execute it
        with open('schema.sql') as f:
            cursor.executescript(f.read())

        connection.commit()
        print("Database initialized successfully.")

    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")

    finally:
        if connection:
            connection.close()

if __name__ == "__main__": 
    db_path = 'database.db'  # Adjust the path if necessary
    initialize_database(db_path)