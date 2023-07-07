import os
import dotenv

dotenv.load_dotenv()

# Access the API key
print(os.getenv('OPENAI_API_KEY'))