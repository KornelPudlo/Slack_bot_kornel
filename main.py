import slack  # Slack client library
import os  # Provides ways to interact with the operating system
import random  # To generate random selections
from pathlib import Path  # Object-oriented filesystem paths
from dotenv import load_dotenv  # To load environment variables from a .env file
from flask import Flask, request, Response  # Flask web framework
from slackeventsapi import SlackEventAdapter  # To handle events from Slack

# Load environment variables from the .env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)  # Create a Flask web app

# Initialize Slack event adapter for handling events like messages
slack_event_adapter = SlackEventAdapter(
    os.environ['SLACK_SIGNING_SECRET'], '/slack/events', app)

# Create a Slack client using the bot token from environment variables
client = slack.WebClient(token=os.environ['SLACK_TOKEN'])

# Retrieve the bot's user ID to recognize mentions in messages
BOT_ID = client.api_call("auth.test")['user_id']

# A dictionary to keep track of message counts per user (for demonstration)
message_counts = {'user_id': 0}

# Lists of image URLs for Dwight Schrute and Walter White to respond with random images
dwight_images = [
    "https://img.nbc.com/files/images/2013/11/12/dwight-500x500.jpg",
    # ... more URLs
]

walter_images = [
    "https://www.rollingstone.com/wp-content/uploads/2018/06/rs-18047-092513-bb-score-623-1380137809.jpg?w=623",
    # ... more URLs
]

# Handle message events from Slack
@slack_event_adapter.on('message')
def message(payload):
    event = payload.get('event', {})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')

    # If the bot is mentioned with "schrute me", send a random Dwight image
    if f'<@{BOT_ID}>' in text and "schrute me" in text.lower():
        dwight_image = random.choice(dwight_images)
        client.chat_postMessage(channel=channel_id, blocks=[
            {"type": "image", "image_url": dwight_image, "alt_text": "Dwight Schrute"}
        ])
        return

    # If the bot is mentioned with "i am the danger", send a random Walter White image
    if f'<@{BOT_ID}>' in text and "i am the danger" in text.lower():
        walter_image = random.choice(walter_images)
        client.chat_postMessage(channel=channel_id, blocks=[
            {"type": "image", "image_url": walter_image, "alt_text": "Walter White"}
        ])
        return

    # Provide information on what commands the user can use with the bot
    if f'<@{BOT_ID}>' in text and "what can i do here?" in text.lower():
        # Detailed response on available commands
        commands_response = "You can do all sorts of things here! ... (more instructions)"
        client.chat_postMessage(channel=channel_id, blocks=[
            {"type": "section", "text": {"type": "mrkdwn", "text": commands_response}}
        ])
        return

    # General interaction based on simple text commands like "hi", "tell me a joke", etc.
    if BOT_ID != user_id:  # Ensure the bot doesn't respond to its own messages
        # Simple greetings and responses
        if text.lower() == 'hi':
            client.chat_postMessage(channel=channel_id, text="Hi! Type @Kornel_Slack_BOT what can I do here? to get started!")
        elif text.lower() == 'tell me a joke':
            jokes = ["Why don't scientists trust atoms? Because they make up everything!", "... more jokes"]
            joke = random.choice(jokes)
            client.chat_postMessage(channel=channel_id, text=joke)
        # ... handle more commands as needed

# Flask route for a slash command to count messages from a user
@app.route('/message-count', methods=['POST'])
def message_count():
    data = request.form
    user_id = data.get('user_id')
    channel_id = data.get('channel_id')
    message_count = message_counts.get(user_id, 0)
    client.chat_postMessage(channel=channel_id, text="You have sent " + str(message_count) + " messages to me.")
    return Response(), 200

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
