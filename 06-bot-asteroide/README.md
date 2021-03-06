# 06-bot-asteroide

| Capitolo precedente                                                                                                                                          | Capitolo successivo                                                                           |
| :--------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------: |
| [◀︎ 05-registrazione-webhook](../05-registrazione-webhook)  | [07-bot-nasa ▶︎](../07-bot-nasa) |

## Obiettivo

In questo capitolo vogliamo fare in modo che qualsiasi cosa scriva un utente, il bot risponda con "asteroide".

## Steps

#### 1. Funzione Post risponde con asteroide

Sei libera di rispondere con qualsiasi cosa, non deve essere necessariamente "asteroide", basta modificare il testo dentro `text="asteroide"`.

- Inserisci il seguente codice
``` py
from http.server import BaseHTTPRequestHandler
from telegram import Bot
import json
import urllib.request

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    token='TOKEN_TELEGRAM_BOT'
    url = 'https://VERCEL_URL/api/bot/'
    bot = Bot(token=token)
    res = bot.setWebhook(url)
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(str(res).encode())
    return

  def do_POST(self):
    content_length = int(self.headers["Content-Length"])
    post_data = self.rfile.read(content_length).decode('utf-8')
    data = json.loads(post_data)
    token='TOKEN_TELEGRAM_BOT'
    bot = Bot(token=token)
    chat_id = data['message']['chat']['id']
    bot.sendMessage(chat_id=chat_id, text="asteroide")
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(str('ok').encode())
    return
```

- Sostituisci `TOKEN_TELEGRAM_BOT` con il codice ricevuto prima dal Botfather
- Sostituisci `VERCEL_URL` con l'url che ti ha dato Vercel

<kbd>![15-bot-asteroide.png](../assets/Lessons/15-bot-asteroide.png)</kbd>

#### 2. Metti online la funzione per registrare il webhook

- Per pubblicare online la funzione creata basta eseguire questo comando
```
vercel --prod
```

#### 3. Trova il tuo bot
- Da cellulare o web entra su Telegram e cerca il bot creato tramite username

<kbd>![16-add-bot-from-telegram](../assets/Lessons/16-add-bot-from-telegram.png)</kbd>

#### 4. Vai a chattare con il tuo bot
- Manda un qualsiasi messaggio
<kbd>![16-add-bot-from-telegram](../assets/Lessons/18-telegram-asteroide-bot.png)</kbd>


| Capitolo precedente                                                                                                                                          | Capitolo successivo                                                                           |
| :--------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------: |
| [◀︎ 05-registrazione-webhook](../05-registrazione-webhook)  | [07-bot-nasa ▶︎](../07-bot-nasa) |