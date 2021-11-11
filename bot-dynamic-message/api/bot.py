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
    contents = json.loads(urllib.request.urlopen('https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY').read())
    chat_id = data['message']['chat']['id']
    bot.sendMessage(chat_id=chat_id, text=contents['url'])
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(str('ok').encode())
    return

