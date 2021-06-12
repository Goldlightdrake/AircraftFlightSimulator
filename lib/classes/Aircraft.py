from lib.classes.FlyingMashine import FlyingMashine


class Aircraft(FlyingMashine):

    def __init__(self, id, name, departure_time, goal_airport, position):
        super().__init__(id, name, departure_time, goal_airport, position)

    def __str__(self):
        return f"Aircraft [ {super().__str__()} ]"

    @staticmethod
    def from_dict(map, start_position):
        print(map)
        return Aircraft(
            id=map['icao24'],
            name=map['callsign'],
            departure_time=map['firstSeen'],
            goal_airport=map['estArrivalAirport'],
            position=start_position
        )
