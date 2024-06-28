from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()


def generate_q_a(theme_doc):
    prompt = [
        f"For speech fluency practice, ask a question about the topic '{theme_doc}'.",
        f"Ask another question about '{theme_doc}'.",
        f"Ask a third question related to '{theme_doc}'.",
        f"Ask a fourth question about '{theme_doc}'.",
        f"Ask a final question related to '{theme_doc}'."
    ]
    
    
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    messages = [
        {"role": "system", "content": "You are a conversation coach. Ask the user 5 questions for speech fluency practice."}
    ]
    for msg in prompt:
        messages.append({"role": "user", "content": msg})

    try:
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=messages
        )

        response_message = completion.choices[0].message.content

        return response_message

    except ApiError as e:
        return f"OpenAI API Error: {e}"
    except Exception as e:
        return f"Unexpected error: {e}"