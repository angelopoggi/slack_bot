import os
from dotenv import load_dotenv,find_dotenv
from pathlib import Path

try:
    env_file = find_dotenv()
    load_dotenv(env_file)
except:
    raise ("Could not open .env file; please make sure it exsists!")

SLACK_TOKEN = os.environ['SLACK_TOKEN']
DAD_API = os.environ['DAD_API']