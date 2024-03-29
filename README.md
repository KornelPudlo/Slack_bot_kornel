Medium: https://medium.com/@korn.pudlo
LinkedIn: https://www.linkedin.com/in/kornel-pud%C5%82o-a19921b5


This Slack Bot is designed to bring fun and productivity to your Slack workspace. It can respond to various commands, send random images, share jokes, fun facts, trivia, and even count the number of messages a user has sent to the bot.

Features
Mention Commands: Interact with the bot by mentioning it along with specific commands like "Schrute me" to receive a random Dwight Schrute image or "I am the danger" for a Walter White image.
Direct Messages: The bot responds to direct messages with a variety of fun and useful commands, such as sharing jokes, fun facts, or daily challenges.
Slash Command: Use the /message-count slash command to see how many messages you've sent to the bot.
Getting Started
To get this bot up and running in your Slack workspace, follow these steps:

Prerequisites
Python 3.6+
A Slack workspace where you have permissions to add apps

Installation

Clone the repository

git clone https://github.com/your-username/slack-bot-project.git
cd slack-bot-project


Set up a virtual environment (optional but recommended)

python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install the required packages

pip install -r requirements.txt

Create a Slack App
Go to Your Apps on Slack API and create a new app.
Add the Bot User and configure it with the necessary permissions (chat:write, commands, app_mentions:read).
Install the app to your workspace and note down the Bot User OAuth Access Token.
Configure environment variables
Rename .env.example to .env and fill in your Slack App credentials:

SLACK_TOKEN=your-bot-user-oauth-access-token
SLACK_SIGNING_SECRET=your-slack-signing-secret
Usage
Run the Flask app:

flask run

The bot should now be running in your Slack workspace. Try mentioning the bot with "@YourBotName what can I do here?" to see what commands are available.

Deployment
To deploy this bot for continuous use, you'll need to host it on a cloud provider like Heroku, AWS, or GCP and set up a public endpoint for Slack events.

Contributing
Contributions are welcome! Feel free to open a pull request or an issue if you have suggestions or find a bug.
