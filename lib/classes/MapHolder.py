import datetime

from lib.classes.Aircraft import Aircraft
from lib.classes.Airport import Airport
from lib.classes.Vector import Vector


class MapHolder:
    """
    MapHolder class made for maintaining gui map for whole time object is holding:
    - List of airports (showing on map)
    - List of aircrafts (showing on map)
    - Selected aircraft (selected by user throw gui)
    - Selected airplane (selected by user throw gui)
    example init: MapHolder()
    """

    def __init__(self):
        self.__list_of_airports = [
            Airport('EDDF', Vector(545, 452)),
            Airport('EPWA', Vector(725, 410)),
            Airport('LFPG', Vector(450, 470)),
            Airport('LEMD', Vector(320, 600)),
            Airport('EGLL', Vector(415, 410)),
            Airport('LPPT', Vector(240, 600)),
            Airport('LIRF', Vector(618, 580)),
            Airport('EIDW', Vector(330, 370)),
            Airport('LGAV', Vector(820, 630)),
            Airport('LTFM', Vector(900, 570)),
            Airport('ENGM', Vector(568, 282)),
            Airport('LKPR', Vector(640, 440)),
            Airport('ESSA', Vector(645, 292)),
            Airport('LOWW', Vector(655, 480)),
            Airport('EHAM', Vector(500, 410)),
            Airport('UUEE', Vector(920, 320)),
            Airport('UKBB', Vector(855, 420)),
            Airport('BIKF', Vector(270, 150)),
            Airport('EFHK', Vector(720, 255)),
            Airport('EETN', Vector(715, 290)),
            Airport('EVRA', Vector(745, 315)),
            Airport('EYVI', Vector(760, 355)),
            Airport('UMMS', Vector(800, 370)),
            Airport('ULLI', Vector(810, 255)),
            Airport('LHBP', Vector(710, 490)),
            Airport('LDZA', Vector(665, 520)),
            Airport('LSZH', Vector(550, 495)),
            Airport('EBBR', Vector(490, 435)),
            Airport('LTAI', Vector(955, 625)),
            Airport('LTAC', Vector(980, 580)),
            Airport('LTBJ', Vector(885, 620))

        ]
        self.__list_of_aircrafts = []
        self.__selected_aircraft = None
        self.__selected_airport = None

    @property
    def list_of_airports(self):
        return self.__list_of_airports

    @list_of_airports.setter
    def list_of_airports(self, list_of_airports: list[Airport]):
        self.__list_of_airports = list_of_airports

    @property
    def list_of_aircrafts(self):
        return self.__list_of_aircrafts

    def put_aircraft_into_map(self):
        if self.__selected_airport is not None:
            for aircraft in self.__selected_airport.get_list_of_aircrafts:
                if aircraft == self.__selected_aircraft:
                    aircraft.selected = True
                if aircraft.flying and len(self.__selected_airport.get_list_of_aircrafts) > len(self.__list_of_aircrafts):
                    self.__list_of_aircrafts.append(aircraft)

    def remove_aircraft_from_map(self, aircraft: Aircraft):
        self.__list_of_aircrafts.remove(aircraft)

    @property
    def selected_aircraft(self):
        return self.__selected_aircraft

    @selected_aircraft.setter
    def selected_aircraft(self, aircraft: Aircraft):
        self.__selected_aircraft = aircraft

    @property
    def selected_airport(self):
        return self.__selected_airport

    @selected_airport.setter
    def selected_airport(self, airport: Airport):
        self.__selected_airport = airport
