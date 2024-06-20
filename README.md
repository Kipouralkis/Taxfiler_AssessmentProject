# Tax Filing Application Project

## Description

EasyTax! is a simple web application to help you get tax filing advice.

## Prerequisites

- Python 3.6 or later.

## Setup Process

1.  **Clone the Repository:**

    ```shell
    git clone https://github.com/Kipouralkis/Taxfiler_AssessmentProject.git

    ```

2. **Install Dependencies:**

    ```shell
    pip install -r requirements.txt
    ```

_It is advised to make a new virtual environment before installing the requirements_


## Running the Application

### On Windows: 

1. **set the Flask app name to app.py**

    ```shell
    set FLASK_APP = app.py
    ```

2. **(Optionally) Set a port**

    ```shell
    set PORT = 8000
    ```

3. **Run the app**

    ```shell
    flask run
    ```

### On Unix/Linux:

```shell
    export FLASK_APP = app.py
    export PORT = 8000
    flask run
```

## REST API Documentation

### Endpoints

#### 1. `/create`

- **Description:** Endpoint to retrieve tax information from the form

- **Methods:**
    - POST: Gets tax information based on form data.

- **Parameters:**
  - `income` (required): Numeric value representing income.
  - `expenses` (required): Numeric value representing expenses.
  - `filing-status` (required): String representing filing status (`single`, `married-jointly`, `married-separately`, `widower`).
  - `dependents` (required): Numeric value representing number of dependents.
  - `investment-assets` (optional): String describing investment assets.

- **Success Response:**
    -  Status code: 302 (Redirect)
        - Response Body: Redirects to the index page with a success message.

- **Error Response:**
    - Status Code: 200 (OK)
        - Response Body: Renders the index.html template with error messages for missing fields or validation errors.
    - Status Code: 500 (Internal Server Error)
        - Response Body: Displays a database error message if the insertion fails.