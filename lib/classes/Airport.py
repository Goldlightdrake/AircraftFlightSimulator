import asyncio

import pygame

from lib.classes.RequestController import RequestController
from lib.classes.Aircraft import Aircraft
from lib.classes.Vector import Vector


class Airport():
    def __init__(self, name: str, position: Vector):
        self.__name = name
        self.__position = position
        self.__list_of_aircrafts = []
        self.airport_icon = pygame.transform.scale(pygame.image.load('./assets/airport_icon.png').convert_alpha(), (25, 25))

    def __str__(self):
        return f'Airport [ name={self.__name}, position={self.__position}, list_of_aircrafts={self.__list_of_aircrafts} ] '

    def __repr__(self):
        return f'Airport [ name={self.__name}, position={self.__position} ] '

    @property
    def name(self):
        return self.__name

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.__position = position

    @property
    def get_list_of_aircrafts(self):
        return self.__list_of_aircrafts

    def generate_list_of_aircrafts(self):
        request_controller = RequestController(api='https://opensky-network.org/api/flights/departure')
        request_data = request_controller.request(self.__name)
        for aircraft_data in request_data:
            self.__list_of_aircrafts.append(Aircraft.from_dict(aircraft_data, self.__position,))

    def send_out_aircraft(self, time):
        for aircraft in self.__list_of_aircrafts:
            if aircraft.get_departurture_time() >= time:
                aircraft.lodge()

    def draw(self, window):
        self.rect = pygame.Rect(self.position.x, self.position.y, 25, 25)
        window.blit(self.airport_icon, self.airport_icon.get_rect(center=self.rect.center))
