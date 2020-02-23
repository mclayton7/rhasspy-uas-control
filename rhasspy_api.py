import requests
import websockets

class RhasspyApi:
    def __init__(self, server_url):
        super().__init__()
        self.server_url = server_url

    def send_text_to_speech(self, text):
        api_endpoint = 'http://{}/api/speech-to-text'.format(self.server_url)
        print('POST: {}'.format(text))
        response = requests.post(url=api_endpoint, data=str.encode(text))

    async def listen_for_intents(self, aircraft_api, intent_handler):
        uri = 'ws://{}/api/events/intent'.format(self.server_url)
        async with websockets.connect(uri) as websocket:
            while True:
                intent = await websocket.recv()
                intent_handler.handle_intent(intent)