import os
import sqlite3

from flask import Flask, abort, flash, redirect, render_template, request, url_for
from openai_request import get_response

import init_db
import validations


app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'
app_name = "EasyTax!"
db_path = os.path.join(os.path.dirname(__file__), 'database.db')

# Ensure the init_db script runs only once during application startup
if not os.path.exists(db_path):
    init_db.initialize_database(db_path)

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

            flash('Tax information added successfully!', 'success')


            advice = get_response(sanitized_data)
            return render_template('index.html', app_name=app_name, advice=advice)    
        
        except sqlite3.Error as e:
            abort(500, f'Database error: {e}')

    return render_template('index.html', app_name=app_name)


      
# @app.rote('/get_tax_advice', methods = ['POST'])
# def get_tax_advice():
#     if request.method == 'POST':
#         # Collect user inputs
#         income = request.form['income']
#         expenses = request.form['expenses']
#         filing_status = request.form['filing-status']
#         dependents = request.form['dependents']
#         investment_assets = request.form['investment-assets']

#     # Prepare input for the AI model
#     prompt = f"Given income of {income}, expenses of {expenses}, filing status of {filing_status}, {dependents} dependents, and investment assets of {investment_assets}, provide tax advice."

#     # Call the OpenAI API to generate tax advice
#     # try: 
#     #     response = openai.completions.create(

#     #     )



if __name__ == '__main__':
    app.run(debug=True, port=8000)