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


## OpenAI Model Integration

This application integrates an OpenAI model to provide tax adviced based on user provided data. 

## To use the AI feature:

1. Obtain an API key from OpenAI

2. Create a `.env` file in the root directory of your project and add your OpenAI API key:

    ```shell
    OPENAI_API_KEY = 'your-api-key'
    ```
3. Run the application as before


### Integration Explanation

The steps taken to integrate the model into the application were

1. Loading Environment Variables from the .env file and Initializing the OpenAI Client

    ```bash
    load_dotenv()
    client = OpenAI()
    ```

2. Defining a function to get AI response.

    -The function `get_response` is defined to handle interactions with the OpenAI model. It constructs a prompt tailored for tax advice based on user-submitted data.

    ```bash
    def get_response(data):
        # Extract data from user input
        income = data['income']
        expenses = data['expenses']
        filing_status = data['filing_status']
        dependents = data['dependents']
        investment_assets = data['investment_assets']

        try:
            # Create a completion request to the OpenAI API
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an experienced accountant. Your name is Jeff. Your mission is to help people file their taxes as easily as possible. Don't forget to introduce yourself by saying you're Jeff the accountant."},
                    {"role": "user", "content": f"Given income of {income}, expenses of {expenses}, filing status of {filing_status}, {dependents} dependents, and investment assets of {investment_assets}, provide tax advice. Don't forget to include some general hot tips. If investment assets are not provided, consider that there might not be any investments"}
                ]
            )

            if completion.choices:
                return markdown2.markdown(completion.choices[0].message.content)
            else:
                return "No response from API"

        except Exception as e:
            return f"Error from API: {str(e)}"

    ```

3. Endpoint for Handling Submission

    - The `/create` Endpoint handles POST requests from the form, validates and sanitizes input data, stores in the database and uses the `get_response` function to send the data to the AI API.



