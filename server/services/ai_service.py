import markdown2
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

def generate_advice(data):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return "Error: OpenAI API key not available"

    client = OpenAI(api_key=api_key)

    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an experienced accountant named Jeff. "
                        "Your mission is to help people file their taxes easily. "
                        "Introduce yourself as Jeff the accountant."
                    )
                },
                {
                    "role": "user",
                    "content": (
                        f"Given income of {data['income']}, expenses of {data['expenses']}, "
                        f"filing status of {data['filing_status']}, {data['dependents']} dependents, "
                        f"and investment assets of {data['investment_assets']}, provide tax advice. "
                        "Include general hot tips. If investment assets are empty, assume none."
                    )
                }
            ]
        )

        if completion.choices:
            return markdown2.markdown(completion.choices[0].message.content)

        return "No response from API"

    except Exception as e:
        return f"Error from API: {str(e)}"
