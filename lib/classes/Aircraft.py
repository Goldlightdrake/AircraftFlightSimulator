from lib.classes.FlyingMashine import FlyingMashine


class Aircraft(FlyingMashine):

    def __init__(self, id, name, departure_time, goal_airport, position):
        super().__init__(id, name, departure_time, goal_airport, position)

    def __str__(self):
        return f"Aircraft [ {super().__str__()} ]"

    @staticmethod
    def from_dict(dict, start_position):
        return Aircraft(
            id=dict['icao24'],
            name=dict['callsign'],
            departure_time=dict['firstSeen'],
            goal_airport=dict['estArrivalAirport'],
            position=start_position
        )
