
from html import escape

def sanitize_input(data):
    sanitized_data = {}
    for key, value in data.items():
        if isinstance(value, str):
            sanitized_data[key] = escape(value)
        else:
            sanitized_data[key] = value
    return sanitized_data


def validate_input(data):
    errors = {}

    def check_decimals(val):
        # Compare the value to the same value when it has only two decimals
        return val == round(float(val), 2)

    # Validate income
    try:
        income = float(data['income'])
        if not check_decimals(income):
            errors['income'] = 'Income must be a number with up to two decimal points.'
    except ValueError:
        errors['income'] = 'Income must be a number.'

    # Validate Expenses
    try:
        expenses = float(data['expenses'])
        if not check_decimals(expenses):
            errors['expenses'] = 'Expenses must be a number with up to two decimal points.'
    except ValueError:
        errors['expenses'] = 'Expenses must be a number.'

    # Validate filing status
    valid_filing_statuses = ['single', 'married-jointly', 'married-separately',  'widower']
    if data['filing_status'] not in valid_filing_statuses:
        errors['filing_status'] = f'Filing status must be one of {valid_filing_statuses}.'

    # Validate Dependents
    try: 
        deps = int(data['dependents'])
        if deps < 0:
            errors['dependents'] = 'Number of dependants must be a non-negative integer.'
    except:
        errors['dependents'] = 'Dependents must be a number.'
 
    
    try:
        isinstance(data['investment_assets'], str)
        if len(data['investment_assets']) > 500:
            errors['investment_assets'] = 'Investment assets description is too long.'
    except:
        errors['investment_assets'] = 'Investment assets must be text.'


    return errors