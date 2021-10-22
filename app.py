# app.py
from flask import Flask, request, jsonify
from songline import Sendline

token = 'xxxxxxxxxxxxxxxxx' 

app = Flask(__name__)

@app.route('/webhook/', methods=['POST'])
def post_webhook():
    data = request.get_json()
    name = data['name']
    messenger = Sendline(token)
    messenger.sendtext('Tradingview Triggered !!! ' +name)
    return jsonify({'result': 'Success', 'name': name})

@app.route('/')
def index():
    return "<h1>BOT v202110 running !!!</h1>"

if __name__ == '__main__':
    app.run()
