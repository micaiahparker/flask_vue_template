import os
from secrets import token_urlsafe
from dotenv import load_dotenv, find_dotenv

#load .env if available
load_dotenv(find_dotenv())

class Config:
    SECRET_KEY = token_urlsafe()
    ENV = os.environ.copy() #put .env in config
