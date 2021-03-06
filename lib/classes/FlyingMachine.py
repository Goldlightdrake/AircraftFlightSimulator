import math
from abc import ABC
import lib.classes.Vector as vector
from lib.classes.FindAWay import FindAWay


class FlyingMachine(ABC):
    """
        FlyingMaschine class made for checking informations about the aircrafts:
        - id (finding a plane by id)
        - name (showing on map)
        - departure time (fixed time to download planes from API)
        - goal airport (the place of arrival of the aircraft will be shown on the map)
        - position (vector position of the aircraft)
        """

    def __init__(self, id, name, departure_time, goal_airport, position):
        self.__id = id
        self.__name = name
        self.__departure_time = departure_time
        self.__goal_airport = goal_airport
        self.__position = vector.copy(position)
        self.__flying = False
        self.__image = None
        self.__selected = False

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

    @property
    def selected(self):
        return self.__selected

    @selected.setter
    def selected(self, value):
        self.__selected = value

    @property
    def flying(self):
        return self.__flying

    def landed(self):
        self.__flying = False

    def update(self, goal_airport_position):
        radians = math.atan2(goal_airport_position.y - self.__position.y, goal_airport_position.x - self.__position.x)
        distance = int(math.hypot(goal_airport_position.x - self.__position.x, goal_airport_position.y - self.__position.y))

        dx = math.cos(radians)
        dy = math.sin(radians)

        if distance:
            distance -= 1
            self.__position.x += dx/4
            self.__position.y += dy/4
        else:
            self.landed()

    @staticmethod
    def from_dict(dict, start_position):
        pass


