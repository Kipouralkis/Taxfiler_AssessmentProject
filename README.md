# Tax Filing Application Project

## Description

EasyTax! is a simple web application to help you get tax filing advice. By completing a form with your financial information, you can get personalized AI advice!

### Documentation
You can read the full documentation at [Wiki](https://github.com/Kipouralkis/Taxfiler_AssessmentProject/wiki#tax-filing-application-project-documentation-page).


## Prerequisites

- Python 3.8 or later.

## Setup Process

1.  **Clone the Repository:**

    ```shell
    git clone https://github.com/Kipouralkis/Taxfiler_AssessmentProject.git

    ```

2. **Install Dependencies:**

    ```shell
    pip install -r requirements.txt
    ```

3.  **To use the AI feature:**

    1. Obtain an API key from OpenAI
    
    2. Create a `.env` file in the root directory of your project and add your OpenAI API key:
    
        ```shell
        OPENAI_API_KEY = your-api-key
        ```
    
    _**Note**: The app is still able to run without AI advice if you don't have an OpenAI API key._
    
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

## Usage

1. Navigate to http://localhost:5000 to access the homepage.

2. Fill out the form with your financial information:

 - Income
 - Expenses
 - Filing Status
 - Dependents
 - Investment Assets (optional)

3. Submit Form:

    Click the submit button to receive tax advice generated by the OpenAI model based on your inputs.

## REST API Documentation

### Endpoints

#### 1. `/`

- **Description**: Renders the main page of application.
- **Parameters**: None
- **Response**: HTML content rendered by `index.html`.

#### 2. `/create`

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
        - Response Body: - Response Body: Returns with a success message for data insertion to database and redirects to the index page with tax advice generated by OpenAI model.

- **Error Response:**
    - Status Code: 200 (OK)
        - Response Body: Renders the index.html template with error messages for missing fields or validation errors.
    - Status Code: 500 (Internal Server Error)
        - Response Body: Displays a database error message if the insertion fails.


## OpenAI Model Integration

This application integrates an OpenAI model to provide tax adviced based on user provided data. 


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



## Docker

### Prerequisites: 
- Install Docker

### Building the Docker container

1. Inside the repositroy, you will find a Dockerfile. Use this to build a docker image:

    ```bash
    docker buid -t taxfiler .
    ```

2. When the docker image is done building, you can create a container using the following command:

    ```bash
    docker run --name easytax-v1.0 -p 5000:5000 -v taxfiler-db:/app/data -e "OPENAI_API_KEY=your-api-key" taxfiler
    ```

    #### Explanation:

    - `--name easytax-v1.0`: Set a name for your container
    - `docker run`: This command creates and starts a new Docker container.
    - `-p 5000:5000`: Maps port 5000 on the host machine to port 5000 inside the Docker container. You can adjust the ports as necessary.
    - `-v taxfiler-db:/app/data`: Creates a docker volume called taxfiler-db. The volume is used to persist the app data even when a container is deleted. The volume is mounted to /app/data inside the container, where the application expects to find its database.
    - `-e "OPENAI_API_KEY=your-api-key"`: Sets an environment variable inside the container for the OPENAI key.
    - `taxfiler`: Specifies the Docker image to use for running the container.

4. Once the Docker container is running, you can access your application by navigating to http://localhost:5000 in your web browser.


## CI/CD Pipeline

This GitHub Actions workflow consists of two jobs: test and deploy. It runs on each push to the repository, ensuring code changes are tested and deployed as needed.

## Jobs:

1. ### Test

    Test Job: Ensures that the application passes all defined tests before deployment. It sets up a clean Python environment, installs dependencies, and runs pytest to execute tests.
    
    - Runs on: `ubuntu-latest` 

    - Steps:
        1. Checkout code: Checks out the latest code from the repository.
        2. Set up Python: Sets up Python version 3.9.
        3. Install dependencies: Creates a virtual environment (venv), activates it, and installs project dependencies listed in requirements.txt.
        4. Run tests: Activates the virtual environment and runs pytest to execute all tests located in the tests/ directory.

2. ### Deploy

    If all tests from the test job pass successfully, it builds a Docker image of the application and pushes it to GitHub Container Registry, making it available for deployment in a production environment.

    - Condition: Runs only if the test job completes successfully (if: success()).
    - Runs on: ubuntu-latest.

    - Steps: 
        1. Checkout code: Checks out the latest code from the repository.
        2. Log in to GitHub Container Registry: Authenticates with GitHub Container Registry using the REGISTRY_TOKEN secret.
        3. Build and push Docker image: Builds a Docker image and pushes it to GitHub Container Registry.
