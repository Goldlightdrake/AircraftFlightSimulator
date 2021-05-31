class Airport:
    def __init__(self):
        self.__name = None
        self.__position = ()
        self.__list_of_aircrafts = []

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        self.__position = position

    def get_list_of_aircrafts(self):
        return self.__list_of_aircrafts


    def generate_list_of_aircrafts(self):
        #TODO: Stworzyć generator obiektów na podstawie danych z requestu
        pass

    def __send_out_aircraft(self):
        #TODO: Stworzyć funkcje, która ciągle sprawdza czy jest jakiś samolot do wylotu NOW!
        pass