# line-notify-bot-webhook


curl --location --request POST 'http://127.0.0.1:5000/webhook' \
--header 'Content-Type: application/json' \
--data-raw '{"alerts": "{{exchange}}:{{ticker}}, price = {{close}}, volume = {{volume}}","text": "\uD83D\uDD25" }'
