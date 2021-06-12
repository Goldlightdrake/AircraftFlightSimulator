from lib.classes.FlyingMashine import FlyingMashine


class Aircraft(FlyingMashine):

    def __init__(self, id, name, departure_time, goal_airport, position):
        super().__init__(id, name, departure_time, goal_airport, position)

    def __str__(self):
        return f"Aircraft [ {super().__str__()} ]"

    @staticmethod
    def from_dict(data, start_position):
        return Aircraft(
            id=data['icao24'],
            name=data['callsign'],
            departure_time=data['firstSeen'],
            goal_airport=data['estArrivalAirport'],
            position=start_position
        )
