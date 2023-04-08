import openai
import os
from dotenv import load_dotenv
import pathlib


def process_ai_input(user_input):
    openai.api_key = os.environ.get('OPENAI_API_KEY')
    print("Here")
    print(openai.api_key)
    script_directory = pathlib.Path(__file__).parent.resolve()
    prompt_file_path = script_directory / "prompt.txt"

    with open(prompt_file_path, "r", encoding="utf-8") as file:
        prompt_text = file.read().strip()
    
    prompt = f"{prompt_text} {user_input}"
    
    messages = [
        {"role": "user", "content": prompt}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=800,
        n=1,
        stop=None,
        temperature=0.7,
    )

    return response.choices[0].message.content.strip()
