from telethon import TelegramClient, events
import json
import time

print('\033[31m Loading cfg.json \033[0m')
with open('cfg.json', 'r') as cfg:
  cfg = json.load(cfg)
  
  # cfg.json variables
  api_id = cfg['api_id']
  api_hash = cfg['api_hash']
  name = cfg['name']
  message = cfg['message']
  timeout = cfg['TIMEOUT']
  
  if not api_id and not api_hash:
    raise Exception('\033[31mYou didn\'t enter the data into the file. cfg.json\033[0m')
print('\033[32m Loading complete \033[0m')


client = TelegramClient(name, api_id, api_hash)
all_user = {}


# NewMessage events
@client.on(events.NewMessage(incoming=True))
async def handler(event):
  if event.is_private:
    cur_time = time.time()
    user = event.sender_id
    if user in all_user:
      if cur_time - all_user[user] < timeout:
        print(f'blocked {user}')
    else:
      await event.reply(message)
      all_user[user] = time.time()
      
# start bot 
client.start()
client.run_until_disconnected()