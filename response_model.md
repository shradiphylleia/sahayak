```
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

def response_arch():
    return os.getenv("API_KEY")

def get_client():
    return genai.Client(api_key=response_arch())

def response_query(prompt_ques: str) -> str:
    """
    Sends the response to the query entered by the user.
    Args:
    prompt_ques (str): user prompt.
    Returns:
    str: model response.
    """
    client = get_client()
    response = client.models.generate_content(
        model='gemini-2.0-flash', contents=prompt_ques
    )
    return response.text if hasattr(response, "text") else str(response)
```
