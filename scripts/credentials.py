# The module is concerned by safely importing credentials as OPENAI Api key

import os
import dotenv

dotenv.load_dotenv()

# Access the API key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')