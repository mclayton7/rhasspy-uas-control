import threading

from point import Point

class AircraftApi:
    def __init__(self, send_text_to_speech):
        super().__init__()
        self.send_text_to_speech = send_text_to_speech
        self._handle_location_received()

    def _handle_location_received(self):
        self.send_text_to_speech("received my location")
        # threading.Timer(10, self._handle_location_received).start()

    def fly_to_point(self, point):
        print('flying to point')

    def stare_at_point(self, point):
        print('setting starepoint')

    def zoom_in(self):
        print('zooming in')

    def zoom_out(self):
        print('zooming out')

    def switch_to_eo(self):
        print('switching to eo')

    def switch_to_ir(self):
        print('switching to ir')

    def switch_to_white_hot(self):
        print('switching to white hot')

    def switch_to_black_hot(self):
        print('switching to black hot')

    def get_aircraft_location(self):
        return Point(0.1, 0.2)

    def get_starepoint_location(self):
        return Point(0.3, 0.4)
