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

    def lodge(self):
        self.__flying = True

    def flying(self):
        return self.__flying

    @staticmethod
    def from_dict(dict, start_position):
        pass


