# Autoresponder for Telegram
## Simple autoresponder for Telegram 

### Installation 
```
git clone https://github.com/djobiden/telegram-autoresponder.git
```

### setup-file
> config.py
```py
api_id=None # api_id
api_hash=None # api_hash
name ="bot_name" # bot name
message="**Autoreply**\nHello! My owner is currently busy. Please wait for their response. All the best!" # message to autoreply
timeout=600 # timeout(in seconds) RECOMENDED > 400
```

### getting api_key api_hash
1. go to the site https://my.telegram.org/auth
2. Log in by entering your number
3. click on <API Development tools>
4. fill in the details to create the application (App title and Short name)
5. Click on <Create Application> at the very bottom
6. now you have two fields <api_key> and <api_hash>, copy each and paste into <config.py>