import time
from telethon import TelegramClient, sync

# Simple Auto claim wave Telegram Bot
# Crafted by cath / viloid (github.com/vsec7)

# Configurations
# Get api_id & api_hash from https://my.telegram.org/
api_id = 24308704
api_hash = 'e6b7f21f4cad657c3de5110434a38a34'

client = TelegramClient('session', api_id, api_hash).start()
to = client.get_entity("waveonsuibot")

def main():	
  client.send_message(entity=to, message="claim Now")
  time.sleep(10)
  msg = client.get_messages("hiofficialbot")[0].click(0)


while True:
  main()
  time.sleep(7200) # 7200 seconds = 2 hours 
