from lib.classes.FlyingMashine import FlyingMashine


class Aircraft(FlyingMashine):

    def __init__(self, id, name, departure_time, goal_airport, position):
        super().__init__(id, name, departure_time, goal_airport, position)

    def __str__(self):
        return f"Aircraft [ {super().__str__()} ]"

    @property
    def id(self):
        return self.id

    @id.setter
    def id(self, id):
        self.id = id

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name):
        self.name = name

    @property
    def departure_time(self):
        return self.departure_time

    @departure_time.setter
    def departure_time(self, departure_time):
        self.departure_time = departure_time
    @property
    def goal_airport(self):
        return self.goal_airport

    @goal_airport.setter
    def goal_airport(self, goal_airport):
        self.goal_airport= goal_airport

    @property
    def position(self):
        return self.position

    @position.setter
    def position(self, position):
        self.position.append(position)

    @staticmethod
    def from_dict(map, start_position):
        return Aircraft(
            id=map['icao24'],
            name=map['callsign'],
            departure_time=map['firstSeen'],
            goal_airport=map['estArrivalAirport'],
            position=start_position
        )
