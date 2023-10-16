import websocket

SOCKET = "wss://stream.binance.com:9443/ws/ethusdt@kline_1m"

def on_open(ws):
    print('opened connection')

def on_close(ws):
    print('closed connection')

def on_message(ws, message):
    print('received message')

try:
    # code that might raise an exception
    ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
    ws.run_forever()
except Exception as e:
    print(e)
