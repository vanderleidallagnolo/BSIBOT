import websocket

SOCKET = "wss://stream.binance.com:9443/ws/ethusdt@kline_1m>"

def on_open():
    print('opened connection')

def on_close():
    print('close connection')

def on_message():
    print('received message')

ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)