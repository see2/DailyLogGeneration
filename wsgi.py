from app.main import app
import os
import uvicorn
from dotenv import load_dotenv
load_dotenv()

api_key = os.environ.get('OPENAI_API_KEY')
print('API Key:', api_key)


if __name__ == "__main__":
    host = "0.0.0.0"
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run("app.main:app", host=host, port=port)