from abc import ABC

class FlyingMashine(ABC):

    def __init__(self, id, name, departure_time, goal_airport, position):
        self.__id = id
        self.__name = name
        self.__departure_time = departure_time
        self.__goal_airport = goal_airport
        self.__position = position
        self.__flying = False

    def __str__(self):
        return f"id={self.__id}, name={self.__name}, departure_time={self.__departure_time}, goal_airport={self.__goal_airport}, position={self.__position}"

    @property
    def name(self):
        return self.__name

    @property
    def departure_time(self):
        return self.__departure_time

    @property
    def goal_airport(self):
        return self.__goal_airport

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_position):
        self.__position = new_position

    def lodge(self):
        self.__flying = True

    def flying(self):
        return self.__flying

    @staticmethod
    def from_dict(dict, start_position):
        pass


