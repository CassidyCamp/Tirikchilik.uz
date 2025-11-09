import os
from dotenv import load_dotenv

if not os.path.exists('database'):
    os.mkdir('database')

load_dotenv()

class Settings:
    TOKEN = os.getenv("TOKEN")
    DataUser = os.getenv("DataUser")
    DataUserpPhone = os.getenv("DataUserpPhone")
    wep_app = os.getenv("wep_app")
