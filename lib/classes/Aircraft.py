import pygame

from lib.classes.FlyingMachine import FlyingMachine
from lib.classes.Vector import Vector


class Aircraft(FlyingMachine):

    def __init__(self, id, name, departure_time, goal_airport, position):
        super().__init__(id, name, departure_time, goal_airport, position)
        self.__image = pygame.transform.scale(pygame.image.load('./assets/aircraft.png').convert_alpha(), (25, 25))
        self.__image_selected = pygame.transform.scale(pygame.image.load('./assets/selected_aircraft.png').convert_alpha(), (25, 25))

    def __str__(self):
        return f"Aircraft [ {super().__str__()} ]"

    def __eq__(self, other):
        if (isinstance(other, Aircraft)):
            return FlyingMachine.name == other.name and FlyingMachine.goal_airport == other.goal_airport
        return False

    @staticmethod
    def from_dict(data: dict, start_position: Vector):
        return Aircraft(
            id=data['icao24'],
            name=data['callsign'],
            departure_time=data['firstSeen'],
            goal_airport=data['estArrivalAirport'],
            position=start_position
        )

    def draw(self, screen):
        top_left_position = self.position
        if self.selected:
            screen.blit(self.__image_selected, top_left_position.make_int_tuple())
            return
        screen.blit(self.__image, top_left_position.make_int_tuple())