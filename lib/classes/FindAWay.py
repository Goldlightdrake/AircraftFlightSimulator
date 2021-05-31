from lib.classes.Vector import Vector


class FindAWay:

    @staticmethod
    def calculate_path(goal_airport_position: tuple[float, float], start_airport_position: tuple[float, float]):
        if goal_airport_position == start_airport_position:
            return 0
        return Vector(goal_airport_position[0], goal_airport_position[1]) - Vector(start_airport_position[0], start_airport_position[1])

