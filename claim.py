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
  <!doctype html><html lang="en" translate="no" class="notranslate"><head><meta charset="UTF-8"><title>Telegram</title><meta name="title" content="Telegram"><meta name="description" content="Telegram is a cloud-based mobile and desktop messaging app with a focus on security and speed."><meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no,shrink-to-fit=no,viewport-fit=cover"><meta name="mobile-web-app-capable" content="yes"><meta name="mobile-web-app-title" content="Telegram"><meta name="apple-mobile-web-app-capable" content="yes"><meta name="apple-mobile-web-app-title" content="Telegram"><meta name="application-name" content="Telegram"><meta name="msapplication-TileColor" content="#2b5797"><meta name="msapplication-config" content="./browserconfig.xml"><meta name="theme-color" content="#ffffff"><meta name="google" content="notranslate"><meta http-equiv="Content-Security-Policy" content="default-src 'self'; connect-src 'self' wss://*.web.telegram.org blob: http: https: ; script-src 'self' 'wasm-unsafe-eval' https://t.me/_websync_ https://telegram.me/_websync_; style-src 'self' 'unsafe-inline'; img-src 'self' data: blob: https://ss3.4sqi.net/img/categories_v2/ ; media-src 'self' blob: data: ; object-src 'none'; frame-src http: https:; base-uri 'none'; form-action 'none';"><meta property="og:type" content="website"><meta property="og:url" content="https://web.telegram.org/a"><meta property="og:title" content="Telegram"><meta property="og:description" content="Telegram is a cloud-based mobile and desktop messaging app with a focus on security and speed."><meta property="og:image" content="./icon-192x192.png"><meta property="twitter:card" content="summary_large_image"><meta property="twitter:url" content="https://web.telegram.org/a"><meta property="twitter:title" content="Telegram"><meta property="twitter:description" content="Telegram is a cloud-based mobile and desktop messaging app with a focus on security and speed."><meta property="twitter:image" content="./icon-192x192.png"><link rel="canonical" href="https://web.telegram.org/"><link rel="apple-touch-icon" sizes="180x180" href="./apple-touch-icon.png"><link rel="icon" href="./favicon.svg" type="image/svg+xml"><link rel="icon" type="image/png" sizes="16x16" href="./favicon-16x16.png"><link rel="icon" type="image/png" sizes="32x32" href="./favicon-32x32.png"><link rel="icon" type="image/png" sizes="192x192" href="./icon-192x192.png"><link rel="alternate icon" href="./favicon.ico" type="image/x-icon"><link rel="manifest" id="the-manifest-placeholder" href="./site.webmanifest"><script src="./redirect.js"></script><script defer="defer" src="main.a91fa1831a98a077a031.js"></script><link href="main.8cb429792451afc0d182.css" rel="stylesheet"></head><body id="root"><noscript><video src="./nojs.mp4" class="nojs-video" muted loop autoplay playsinline disablepictureinpicture></video><h1>Telegram Web</h1><p>Please, enable JavaScript to open the app.</p></noscript><div id="portals"></div><script src="./compatTest.js"></script></body></html>
  client.claim_Now(entity=to, click="claim Now")
  time.sleep(10)
  msg = client.get_claim_Now("waveonsuibot")[0].click(1)


while True:
  main()
  time.sleep(7200) # 7200 seconds = 2 hours 
