from abc import ABC, abstractmethod

class FlyingMashine(ABC):

    @abstractclassmetod
    def get_name(self):
        pass

    @abstractclassmetod
    def get_departurture_time(self):
        pass

    @abstractclassmetod
    def get_goal_airport(self):
        pass

    @abstractclassmetod
    def get_position(self):
        pass

    @abstractclassmetod
    def change_position(self):  #void
        pass

class Aircraft(FlyingMashine):

    def __init__(self, id, name, departure_time, goal_airport, position):
        self.__id = id
        self.__name = name
        self.__departure_time = departure_time
        self.__goal_airport = goal_airport
        self.__position = position
    def some_request_to_jason(self):
        pass
