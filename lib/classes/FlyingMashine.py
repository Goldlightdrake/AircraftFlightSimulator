from abc import ABC, abstractmethod

class FlyingMashine(ABC):

    @abstractclassmetod
    def get_name(self):
        pass

    @abstractclassmetod
    def get_departurture_time(self):
        pass

    @abstractclassmetod
    def get_goal_airport(self):
        pass

    @abstractclassmetod
    def get_position(self):
        pass

    @abstractclassmetod
    def change_position(self):  #void
        pass
