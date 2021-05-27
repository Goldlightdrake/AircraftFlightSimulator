class MapHolder:
    def __init__(self):
        self.__list_of_airports = []
        self.__list_of_aircrafts = []
        self.__selected_aircraft = None
        self.__selected_airport = None

    @property
    def list_of_airports(self):
        return self.__list_of_aircrafts

    @list_of_airports.setter
    def list_of_airports(self, list_of_airports):
        self.__list_of_airports = list_of_airports

    @property
    def list_of_aircrafts(self):
        return self.__list_of_aircrafts

    def put_aircraft_into_map(self, aircraft):
        self.__list_of_aircrafts.append(aircraft)

    @property
    def selected_aircraft(self):
        return self.__selected_aircraft

    @selected_aircraft.setter
    def selected_aircraft(self, aircraft):
        self.__selected_aircraft = aircraft

    @property
    def selected_airport(self):
        return self.__selected_airport

    @selected_airport.setter
    def selected_airport(self, airport):
        self.__selected_airport = airport

