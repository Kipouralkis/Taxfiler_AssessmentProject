import markdown2
from openai import OpenAI
from dotenv import load_dotenv

# get openAI key from local .env
load_dotenv()
client = OpenAI()

def get_response(data):


    income = data['income']
    expenses = data['expenses']
    filing_status = data['filing_status']
    dependents = data['dependents']
    investment_assets = data['investment_assets']

    try: 
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an experienced accountant. Your name is Jeff. Your mission is to help people file their taxes as easily as possible. Don't forget to introduce yourself by saying you're Jeff the accountant."},
                {"role": "user", "content": f"Given income of {income}, expenses of {expenses}, filing status of {filing_status}, {dependents} dependents, and investment assets of {investment_assets}, provide tax advice. Don't forget to include some general hot tips. If investment assets are not provided, consider that there might not be any investments" }
            ]
        )

        if completion.choices:
            return markdown2.markdown(completion.choices[0].message.content)
        else:
            return "No response from API"
        
    except Exception as e:
        return f"Error from API: {str(e)}"