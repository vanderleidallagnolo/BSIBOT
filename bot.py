import websocket, json, pprint

SOCKET = "wss://stream.binance.com:9443/ws/ethusdt@kline_1m"

def on_open(ws):
    print('opened connection')

def on_close(ws):
    print('closed connection')

def on_message(ws, message):
    print('received message')
    # print(message)
    json_message = json.loads(message)
    #print(json_message)
    pprint.pprint(json_message)

    candle = message['k']

    is_candle_closed = candle['x']

    close = candle['c']

    if is_candle_closed:
        print('candle closed at {}', format(close))

try:
    # code that might raise an exception
    ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
    ws.run_forever()
except Exception as e:
    print(e)
