###
# Obviously the .env file for the app has to be on the same level or specified
# when calling 'load_dotenv()'

from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    VALID_UP_PAIRS = os.getenv("VALID_USERNAME_PASSWORD_PAIRS")
    USER_SETTINGS = os.getenv("USER_SETTINGS")
    UPLOAD_PATH = os.getenv("UPLOAD_PATH")
    API_BASE = os.getenv("API_base_url")
    API_END = os.getenv("API_endpoint")
    API_KEY = os.getenv("API_key")
    TARGET_SITE = os.getenv("TARGET_site")
    