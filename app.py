#!/usr/bin/env python

import asyncio
import websockets

from aircraft_api import AircraftApi
from intent_handler import IntentHandler
from rhasspy_api import RhasspyApi

RHASSPY_SERVER = '192.168.7.59:12101'

async def main():
    rhasspy_api = RhasspyApi(RHASSPY_SERVER)
    aircraft_api = AircraftApi(rhasspy_api.send_text_to_speech)
    intent_handler = IntentHandler(aircraft_api, rhasspy_api.send_text_to_speech)
    await rhasspy_api.listen_for_intents(aircraft_api, intent_handler)

asyncio.run(main())