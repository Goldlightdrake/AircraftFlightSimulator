class Aircraft(FlyingMashine):

    def __init__(self, id, name, departure_time, goal_airport, position):
        self.__id = id
        self.__name = name
        self.__departure_time = departure_time
        self.__goal_airport = goal_airport
        self.__position = position
    def some_request_to_jason