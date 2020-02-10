import aiohttp
import unittest
import requests

RHASSPY_SERVER = '192.168.7.59:12101'

def post_text_to_intent(text):
    api_endpoint = 'http://{}/api/text-to-intent'.format(RHASSPY_SERVER)
    print('POST: {}'.format(text))
    response = requests.post(url=api_endpoint, data=str.encode(text))


class IntegrationTests(unittest.TestCase):
    def test_fly_home(self):
        text = 'fly home'
        post_text_to_intent(text)
        self.assertEqual(1, 2)