import os
import sys
import tempfile
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from app import app, init_db


# Set up a temporary database for testing
@pytest.fixture
def client():
    # Use a temporary database for testing
    db_fd, db_path = tempfile.mkstemp()
    app.config['TESTING'] = True
    app.config['DATABASE'] = db_path

    with app.test_client() as client:
        with app.app_context():
            init_db.initialize_database(db_path)
        yield client

    os.close(db_fd)
    os.unlink(db_path)

# Test index route
def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to EasyTax!' in response.data

# Test create route with valid data
# def test_create_valid(client):
#     data = {
#         'income': '50000',
#         'expenses': '25000',
#         'filing-status': 'single',
#         'dependents': '2',
#         'investment-assets': '100000'
#     }
#     response = client.post('/create', data=data, follow_redirects=True)
#     assert response.status_code == 200
#     assert b'Tax information added successfully!' in response.data
#     assert b'Your Tax Advice' in response.data 

# Test create route with missing fields
def test_create_missing_fields(client):
    data = {
        'income': '',
        'expenses': '25000',
        'filing-status': 'single',
        'dependents': '2',
        'investment-assets': '100000'
    }
    response = client.post('/create', data=data, follow_redirects=True)
    assert b'Missing required fields' in response.data

    #
    