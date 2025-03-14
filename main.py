from telethon import TelegramClient, events
from config import *
import json
import time

# Loading config file(Examination)
print('\033[31m Loading config.py \033[0m')
if not api_id and not api_hash:
  raise Exception('\033[31mYou didn\'t enter the data into the file. config.py\033[0m')
print('\033[32m Loading complete \033[0m')

# client
client = TelegramClient(name, api_id, api_hash)
all_user = {}

# NewMessage events
@client.on(events.NewMessage(incoming=True))
async def handler(event):
  if event.is_private:
    cur_time = time.time()
    sender = await event.get_sender()
    user = event.sender_id
    if user in all_user:
      if cur_time - all_user[user] < timeout:
        print(f'blocked request from user {user} | {sender.username}')
    else:
      await event.reply(message)
      all_user[user] = time.time()
      
# start bot 
client.start()
client.run_until_disconnected()