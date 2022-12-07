from flask import Flask, request
from revChatGPT.revChatGPT import Chatbot
import os
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
import threading
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)

client = Client(os.environ['TWILIO_SID'], os.environ['TWILIO_TOKEN'])

config = {
  "Authorization": "<Your Bearer Token Here>",
  "session_token": os.environ['SESSION_TOKEN']
}


def getChatResponse(prompt, number, twilio_number):
  chatbot = Chatbot(config, conversation_id=None)
  chatbot.reset_chat()
  chatbot.refresh_session()
  message = chatbot.get_chat_response(prompt)
  client.messages.create(to=number,
                         from_=twilio_number,
                         body=message['message'][:1600])
  return(None)


@app.route('/')
def index():
  return ("This is a backend service. You'll need to add your own OpenAI session token and Twilio credentials")


@app.route('/sms', methods=['POST'])
def sms():
  message = request.form['Body']
  phone_number = request.form['From']
  twilio = request.form['To']

  thread = threading.Thread(target=getChatResponse,
                            args=(message, phone_number, twilio))
  thread.start()

  return ("200")


@app.route('/timeout', methods=['POST'])
def timeout():
  phone_number = request.form['From']
  twilio = request.form['To']

  client.messages.create(to=phone_number,
                         from_=twilio,
                         body="Sorry an error occured")

  return ("timeout")


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
