class Airport:
    def __init__(self):
        self.__name = None
        self.__position = []
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
        self.__position.append() #double
    @property
    def get_list_of_aircrafts(self):
        return self.__list_of_aircrafts


    def generate_list_of_aircrafts(self): #void inicjalizator do stworzenia obiektow aircraftu
        return self.get_list_of_aircrafts  #zadać pytaie do request on daje dictionary, stowrzyc obiekty dodaje do listy

    def __send_out_aircraft(self): #void
        return True   #while true sprawdzac czy departure time od aircraft na teraz