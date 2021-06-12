import pygame

from lib.classes.Airport import Airport

class AirportView:
    def __init__(self, airport: Airport):
        self.airport = airport
        self.airport_icon = pygame.transform.scale(pygame.image.load('../gui/assets/airport_icon.png').convert_alpha(), (25,25))

    def draw(self, window):
        self.rect = pygame.Rect(self.airport.position[0], self.airport.position[1], 25, 25)
        window.blit(self.airport_icon, self.airport_icon.get_rect(center=self.rect.center))
