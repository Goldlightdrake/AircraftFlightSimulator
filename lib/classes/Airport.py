import time

from RequestController import RequestController
from Aircraft import Aircraft


class Airport:
    def __init__(self, name: str, position: tuple):
        self.__name = name
        self.__position = position
        self.__list_of_aircrafts = []

    @property
    def name(self):
        return self.__name

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.__position = position

    def get_list_of_aircrafts(self):
        return self.__list_of_aircrafts

    def generate_list_of_aircrafts(self):
        request_controller = RequestController(api='https://opensky-network.org/api/flights/departure?')
        request_data = request_controller.request(self.__name)
        for aircraft_data in request_data:
            print(aircraft_data)
            self.__list_of_aircrafts.append(Aircraft.from_dict(aircraft_data, self.__position,))

    def __send_out_aircraft(self):
        for aircraft in self.__list_of_aircrafts:
            if aircraft.get_departurture_time() == time.time():
                aircraft.lodge()
