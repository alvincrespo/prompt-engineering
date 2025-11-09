from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

def get_response(prompt):
    """
    Get a response from OpenAI's GPT model using the provided prompt.

    Args:
        prompt (str): The prompt to send to the model

    Returns:
        str: The model's response content
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return response.choices[0].message.content
