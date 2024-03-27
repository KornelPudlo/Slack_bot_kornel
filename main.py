import slack
import os
from pathlib import Path
from dotenv import load_dotenv

#where the path for the .env file is stored
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

client = slack.WebClient(token=os.environ['SLACK_TOKEN'])

client.chat_postMessage(channel='#slack_bot_kornel', text="Hello end-users! I am a bot!")
