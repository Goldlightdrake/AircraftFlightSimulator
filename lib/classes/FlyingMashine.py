from abc import ABC

class FlyingMashine(ABC):

    def __init__(self, id, name, departure_time, goal_airport, position):
        self.__id = id
        self.__name = name
        self.__departure_time = departure_time
        self.__goal_airport = goal_airport
        self.__position = position

    def get_name(self):
        pass

    def get_departurture_time(self):
        pass

    def get_goal_airport(self):
        pass

    def get_position(self):
        pass

    def change_position(self):
        pass


