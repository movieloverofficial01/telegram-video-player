import os
import requests
from flask import Flask, request

TOKEN = os.environ['8086038655:AAG5FfTAz-WVV-xpdi64UZrUm8aWsm1U7DA']
CHANNEL = os.environ['@movielover322']  # যেমন @your_channel_username
API = f'https://api.telegram.org/bot{TOKEN}'

app = Flask(__name__)


@app.route('/')
def home():
    return 'Bot is running'


@app.route('/webhook', methods=['POST'])
def webhook():
    update = request.get_json(silent=True) or {}
    msg = update.get('message')
    if not msg:
        return 'ok'

    chat_id = msg['chat']['id']
    text = msg.get('text', '')

    if text.startswith('/start '):
        arg = text.split(' ', 1)[1].strip()
        if arg.isdigit():
            requests.post(f'{API}/copyMessage', json={
                'chat_id': chat_id,
                'from_chat_id': CHANNEL,
                'message_id': int(arg),
            })
    elif text == '/start':
        requests.post(f'{API}/sendMessage', json={
            'chat_id': chat_id,
            'text': 'ভিডিওর লিংকে ক্লিক করে এখানে আসুন।',
        })
    return 'ok'
