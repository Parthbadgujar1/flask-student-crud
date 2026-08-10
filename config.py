import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "my-super-secret-key")
    
    # SQLite database
    SQLALCHEMY_DATABASE_URI = "sqlite:///students.db"
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False