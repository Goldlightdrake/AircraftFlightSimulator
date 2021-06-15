import pygame

class Menu():
    def __init__(self, simulation):
        self.simulation = simulation
        self.mid_w, self.mid_h = self.simulation.DISPLAY_W / 2, self.simulation.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 50, 20)
        self.offset = - 100

    def draw_cursor(self):
        self.simulation.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.simulation.window.blit(self.simulation.display, (0, 0))
        pygame.display.update()
        self.simulation.reset_keys()

class MainMenu(Menu):
    def __init__(self, simulation):
        Menu.__init__(self, simulation)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 40
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 70
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 100
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
        self.menu_background = pygame.transform.scale(pygame.image.load("./assets/menu_background.jpg"), (self.simulation.DISPLAY_W, self.simulation.DISPLAY_H))

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.simulation.check_events()
            self.check_input()
            self.simulation.display.blit(self.menu_background, (0,0))
            self.simulation.draw_text('Aircraft Scanner Simulator', 25, self.simulation.DISPLAY_W / 2, self.simulation.DISPLAY_H / 2 - 20)
            self.simulation.draw_text("Rozpocznij symulacje", 20, self.startx, self.starty)
            self.simulation.draw_text("Opcje", 20, self.optionsx, self.optionsy)
            self.simulation.draw_text("Autorzy", 20, self.creditsx, self.creditsy)
            self.draw_cursor()
            self.blit_screen()


    def move_cursor(self):
        if self.simulation.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
        elif self.simulation.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'

    def check_input(self):
        self.move_cursor()
        if self.simulation.START_KEY:
            if self.state == 'Start':
                self.simulation.simulating = True
            elif self.state == 'Options':
                self.simulation.curr_menu = self.simulation.options
            elif self.state == 'Credits':
                self.simulation.curr_menu = self.simulation.credits
            self.run_display = False

class OptionsMenu(Menu):
    def __init__(self, simulation):
        Menu.__init__(self, simulation)
        self.state = 'Volume'
        self.volx, self.voly = self.mid_w, self.mid_h + 20
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.simulation.check_events()
            self.check_input()
            self.simulation.display.fill((0, 0, 0))
            self.simulation.draw_text("Opcje", 20, self.simulation.DISPLAY_W / 2, self.simulation.DISPLAY_H / 2 - 30)
            self.simulation.draw_text("Głośność", 15, self.volx, self.voly)
            self.simulation.draw_text("Kontrola", 15, self.controlsx, self.controlsy)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.simulation.BACK_KEY:
            self.simulation.curr_menu = self.simulation.main_menu
            self.run_display = False
        elif self.simulation.UP_KEY or self.simulation.DOWN_KEY:
            if self.state == 'Volume':
                self.state = 'Controls'
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
            elif self.state == 'Controls':
                self.state = 'Volume'
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
        elif self.simulation.START_KEY:
            # TO-DO: Create a Volume Menu and a Controls Menu
            pass

class CreditsMenu(Menu):
    def __init__(self, simulation):
        Menu.__init__(self, simulation)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.simulation.check_events()
            if self.simulation.START_KEY or self.simulation.BACK_KEY:
                self.simulation.curr_menu = self.simulation.main_menu
                self.run_display = False
            self.simulation.display.fill(self.simulation.BLACK)
            self.simulation.draw_text('Autorzy', 35, self.simulation.DISPLAY_W / 2, self.simulation.DISPLAY_H / 2 - 20)
            self.simulation.draw_text('Piotr Graczyk', 20, self.simulation.DISPLAY_W / 2, self.simulation.DISPLAY_H / 2 + 30)
            self.simulation.draw_text('Zofia Żukowicz', 20, self.simulation.DISPLAY_W / 2, self.simulation.DISPLAY_H / 2 + 60)
            self.blit_screen()
