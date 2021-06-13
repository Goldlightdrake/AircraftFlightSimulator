import pygame

from lib.classes.FlyingMachine import FlyingMachine


class Aircraft(FlyingMachine):

    def __init__(self, id, name, departure_time, goal_airport, position):
        super().__init__(id, name, departure_time, goal_airport, position)
        self.__image = pygame.transform.scale(pygame.image.load('./assets/aircraft.png').convert_alpha(), (25, 25))

    def __str__(self):
        return f"Aircraft [ {super().__str__()} ]"

    @staticmethod
    def from_dict(data, start_position):
        return Aircraft(
            id=data['icao24'],
            name=data['callsign'],
            departure_time=data['firstSeen'],
            goal_airport=data['estArrivalAirport'],
            position=start_position
        )

    def draw(self, screen):
        top_left_position = self.position
        screen.blit(self.__image, top_left_position.make_int_tuple())