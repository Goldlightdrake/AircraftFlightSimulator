import asyncio


from lib.gui.airport_view import AirportView
from menu import *
from lib.classes.MapHolder import MapHolder
from pgu import gui
from lib.classes.Aircraft import Aircraft



class Simulation():
    def __init__(self):
        pygame.init()
        self.running, self.simulating = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 1280, 720
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W, self.DISPLAY_H)))
        self.font_name = 'assets/Montserrat-Bold.ttf'
        #self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu
        self.map_holder = MapHolder()
        self.clock = pygame.time.Clock()
        self.background_image = pygame.transform.scale(pygame.image.load("../gui/assets/background.jpg"), (self.DISPLAY_W, self.DISPLAY_H))

    def simulation_loop(self):
        self.draw_background()
        while self.simulating:
            self.clock.tick(60)
            self.check_events()
            if self.START_KEY:
                self.simulating = False
            pygame.display.update()
            self.reset_keys()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.simulating = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                    print(self.START_KEY)
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if pygame.mouse.get_pressed(3)[0]:
                    for airport in self.map_holder.list_of_airports:
                        rect = pygame.Rect(airport.position[0], airport.position[1], 25, 25)
                        if rect.collidepoint(x, y):
                            self.map_holder.selected_airport = airport
                            self.user_selecting_aircraft()

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)
        self.window.blit(self.display, (0, 0))

    def user_selecting_aircraft(self):
        run = True
        self.window.fill(self.BLACK)
        if not self.map_holder.selected_airport.get_list_of_aircrafts:
            self.map_holder.selected_airport.generate_list_of_aircrafts()
        self.draw_list_of_chosen_airport()
        pygame.display.update()
        while run:
            self.clock.tick(60)
            self.check_events()
            if self.BACK_KEY:
                run = False
            pygame.display.update()
            self.reset_keys()
        self.draw_background()

    def draw_airports(self, list_of_airports):
        for airport in list_of_airports:
            AirportView(airport).draw(window=self.window)

    def draw_background(self):
        self.window.blit(self.background_image, (0, 0))
        self.draw_airports(self.map_holder.list_of_airports)

    def draw_list_of_chosen_airport(self):
        self.check_events()
        self.main_menu.check_input()
        self.display.fill(self.BLACK)
        self.draw_text('Oto twoja lista samolotów: ', 20, 200, 50)
        aircraft_list = self.map_holder.selected_airport.get_list_of_aircrafts
        for index, aircraft in enumerate(aircraft_list):
            self.draw_text(aircraft.name, 20, 200, 80+(index*30))
