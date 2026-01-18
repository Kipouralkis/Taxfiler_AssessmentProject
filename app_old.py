import os
import sqlite3

from flask import Flask, abort, flash, redirect, render_template, request, url_for
from openai_request import get_response

import Taxfiler_AssessmentProject.server.utils.init_db as init_db
import Taxfiler_AssessmentProject.server.utils.validations as validations


app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'
app_name = "EasyTax!"

# data dir
data_dir = os.path.join(os.path.dirname(__file__), 'data')
db_path = os.path.join(data_dir, 'database.db')

# Create database directory
if not os.path.exists(data_dir):
    try:
        os.makedirs(data_dir)  #
    except OSError as e:
        print(f"Failed to create directory: {data_dir} - {e}")

# Ensure the init_db script runs only once during application startup
if not os.path.exists(db_path):
    try:
        init_db.initialize_database(db_path)
    except Exception as e:
        print(f"Error initializing database: {str(e)}")

# Seting up the database connection
def get_db_connection(db_path):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

# Routes

@app.route('/')
def index():
    return render_template('index.html', app_name=app_name,)


@app.route('/create', methods=['POST'])
def create():
    if request.method == 'POST':

        # collect form data in a dictionary
        data = {
            'income': request.form['income'],
            'expenses': request.form['expenses'],
            'filing_status': request.form['filing-status'],
            'dependents': request.form['dependents'],
            'investment_assets': request.form['investment-assets']
        }

        # Check for missing fields
        missing_fields = [field for field, value in data.items() if not value]
        if missing_fields:
            missing_fields_str = ', '.join(missing_fields)
            flash(f'Missing required fields: {missing_fields_str}', 'error')
            return render_template('index.html', app_name=app_name, form_data=data)
        
        # Data validation and sanitization
        sanitized_data = validations.sanitize_input(data)
        errors = validations.validate_input(sanitized_data)

        # If errors, display error message and pass inputed data back to the template
        if errors:
            for _, error in errors.items():
                flash(f"{error}", 'error')
            return render_template('index.html', app_name=app_name, form_data=data, errors=errors)
        
        # Write data to db
        try:
            conn = get_db_connection(db_path)
            cursor = conn.cursor()
            cursor.execute('INSERT INTO taxInfo (income, expenses, filing_status, dependents, investment_assets) VALUES (?, ?, ?, ?, ?)',
                           [sanitized_data[field] for field in ['income', 'expenses', 'filing_status', 'dependents', 'investment_assets']])
            conn.commit()

            conn.close()

            # flash('Tax information added successfully!', 'success')

            # After writting to database has been successful, get AI advice
            advice = get_response(sanitized_data)
            return render_template('index.html', app_name=app_name, advice=advice)    
        
        except sqlite3.Error as e:
            abort(500, f'Database error: {e}')

    return render_template('index.html', app_name=app_name)



if __name__ == '__main__':
    app.run(debug=True, port=8000)