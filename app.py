from flask import Flask, request, abort, jsonify, json
import requests
import time

url = 'https://notify-api.line.me/api/notify'
token = 'xxxxxxxxxxxxxx'
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}
imange = 'https://raw.githubusercontent.com/phonpitsanu/line-notify-bot-webhook/main/doge.png'

app = Flask(__name__)
@app.route('/webhook', methods=['POST'])  
def webhook():
    if request.method == 'POST':
        data = request.get_json()
        alerts = data.get('alerts', '')
        text = data.get('text', '')
        #payload = {'message':alerts, 'imageThumbnail':imange, 'imageFullsize':imange}
        payload = {'message':text+alerts}
        r = requests.post(url, headers=headers, data = payload)
        print (r.text)
        return jsonify(payload)
    else:
        abort(400)

    
@app.route('/')
def index():
    return "<h1>UNMAI BOT v2(line-notify-api) running !!!</h1>"

if __name__ == '__main__':
    app.run()
