import json
from point import Point
from locations import *

HOME = Point(0.12, 0.34, 0.56)
ME = Point(0.78, 0.89, 0.90)


class IntentHandler:
    def __init__(self, aircraft_api, send_text_to_speech):
        super().__init__()
        self.aircraft_api = aircraft_api
        self.send_text_to_speech = send_text_to_speech

    def handle_intent(self, intent):
        x = json.loads(intent)
        intent_name = x['intent']['name']
        entities = x['entities']
        handlers = {
            'FlyMission': self._handle_fly_mission,
            'FlyToMe': self._handle_fly_to_me,
            'FlyToWaypoint': self._handle_fly_to_waypoint,
            'GetAircraftLocation': self._handle_get_aircraft_location,
            'GetStarepointLocation': self._handle_get_aircraft_location,
            'ReturnHome': self._handle_return_home,
            'StareAtwaypoint': self._handle_stare_at_waypoint,
            'SwitchToBlackHot': self._switch_to_black_hot,
            'SwitchToEo': self._switch_to_eo,
            'SwitchToIr': self._switch_to_ir,
            'SwitchToWhiteHot': self._switch_to_white_hot,
            'ZoomIn': self._zoom_in,
            'ZoomOut': self._zoom_out,
        }
        func = handlers.get(
            intent_name, lambda x: print('cannot handle function'))
        func(entities)

    def _handle_fly_mission(self, entities):
        try:
            mission_name = entities['value']
            mission = MISSIONS[mission_name]
        except expression as identifier:
            pass
        self.aircraft_api.fly_mission(mission)
        self.send_text_to_speech('Executing mission {}.'.format(mission_name))

    def _handle_fly_to_me(self, entities):
        self.aircraft_api.fly_to_point(ME)
        self.send_text_to_speech('Flying to you.')

    def _handle_fly_to_waypoint(self, entities):
        try:
            waypoint_name = entities['value']
            point = WAYPOINTS[waypoint_name]
        except expression as identifier:
            pass
        self.aircraft_api.fly_to_point(point)
        self.send_text_to_speech(
            'Flying to waypoint {}.'.format(waypoint_name))

    def _handle_get_aircraft_location(self, entities):
        (lat_rad, lon_rad, alt_msl) = self.aircraft_api.get_aircraft_location()
        self.send_text_to_speech('The location of the aircraft is unknown.')

    def _handle_get_starepoint_location(self, entities):
        (lat_rad, lon_rad, alt_msl) = self.aircraft_api.get_starepoint_location()
        self.send_text_to_speech('The location of the starepoint is unknown.')

    def _handle_return_home(self, entities):
        self.aircraft_api.fly_to_point(HOME)
        self.send_text_to_speech('Flying home.')

    def _handle_stare_at_waypoint(self, entities):
        try:
            waypoint_name = entities['value']
            point = WAYPOINTS[waypoint_name]
        except expression as identifier:
            pass
        self.aircraft_api.stare_at_point(point)
        self.send_text_to_speech(
            'Staring at waypoint {}.'.format(waypoint_name))

    def _switch_to_black_hot(self, entities):
        self.aircraft_api.switch_to_black_hot()
        self.send_text_to_speech('Switching to Black Hot.')

    def _switch_to_eo(self, entities):
        self.aircraft_api.switch_to_eo()
        self.send_text_to_speech('Switching to EO.')

    def _switch_to_ir(self, entities):
        self.aircraft_api.fly_to_point()
        self.send_text_to_speech('Switching to IR.')

    def _switch_to_white_hot(self, entities):
        self.aircraft_api.switch_to_white_hot()
        self.send_text_to_speech('Switching to White Hot.')

    def _zoom_in(self, entities):
        self.aircraft_api.zoom_in()
        self.send_text_to_speech('Zooming in.')

    def _zoom_out(self, entities):
        self.aircraft_api.zoom_out()
        self.send_text_to_speech('Zooming out.')
