from point import Point

ALPHA = Point(0.123, 0.456)
BRAVO = Point(0.234, 0.567)
CHARLIE = Point(0.345, 0.678)
DELTA = Point(0.456, 0.789)

MISSION_ECHO = [ALPHA, BRAVO, CHARLIE, DELTA]
MISSION_FOXTROT = [DELTA, CHARLIE, BRAVO, ALPHA]

WAYPOINTS = {
    'alpha': ALPHA,
    'bravo': BRAVO,
    'charlie': CHARLIE,
    'delta': DELTA,
}

MISSIONS = {
    'echo': MISSION_ECHO,
    'foxtrot': MISSION_FOXTROT,
}
