from lib.classes.FlyingMashine import FlyingMashine


class Aircraft(FlyingMashine):

    def __init__(self, id, name, departure_time, goal_airport, position):
        super().__init__(id, name, departure_time, goal_airport, position)