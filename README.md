# chatGPT Text interface
This is a wrapper around chatGPT so that you can access the platform via text message. 
## Setup
This app requires both a Twilio account and an OpenAI account for this to work. All credentials are stored in a `.env` file. 
<br>
1. Activate your python virtual environment: `python3 -m venv <path to project directory>`
2. Run `pip3 install -r requirements.txt` to install project dependencies
3. Run `mv .env.example .env` create your `.env` file 
<br><br>
## Grab your OpenAI Authentication Token
1. Go to https://chat.openai.com and log in or sign up
2. Open your developer console with `F12` 
3. Open the `Application` tab and click `Cookies` 
4. Copy the value for `__Secret-nextauth.session-token` and paste it to the `.env` file that you have just created under `SESSION_TOKEN`.
<img width="952" alt="image" src="https://user-images.githubusercontent.com/9896624/205768416-9ffb0d37-134d-4022-b0ea-380299b1a13c.png">
<br><br>
## Twilio SID and Secret Token
1) Go to https://www.twilio.com/ and make a Twilio account.
2) Go to your twilio console and you'll see your Twilio SID and secret token.
3) Copy and paste them in your `.env` file as `TWILIO_SID` and `TWILIO_TOKEN` accordingly. 
<br><br>

## Configure a number to your app 
Once your app is publically hosted, you need to buy a Twilio phone number add your url to your Twilio SMS response webhook. 
1) Buy a Twilio phone number
2) In the phone number settings add your webhook urls. The response webhook should be in the format `https://example.com/sms` and the failure webhook is in the format `https://example.com/timeout`
<img width="1234" alt="image" src="https://user-images.githubusercontent.com/9896624/205769800-d57d97f0-9713-47a2-b0e3-4df9b65930b9.png">

--- 
I have a hosted version of the application working. Message me if you would like to text the number that I'm hosting. Works in both Canada and the US
