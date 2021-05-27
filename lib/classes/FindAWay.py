from lib.data.classes.Vector import Vector


class FindAWay:

    def __init__(self):
        pass

    @staticmethod
    def calculate_path(goal_airport_position: tuple[float, float], start_airport_position: tuple[float, float]):
        return Vector(goal_airport_position[0], goal_airport_position[1]) - Vector(start_airport_position[0], start_airport_position[1])