from app.main import app
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.environ.get('OPENAI_API_KEY')
print('API Key:', api_key)
if __name__ == "__main__":
    app.run()
