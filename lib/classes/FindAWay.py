from lib.classes.Vector import Vector


class FindAWay:

    @staticmethod
    def calculate_path(goal_airport_position, start_airport_position):
        if goal_airport_position == start_airport_position:
            return 0
        return goal_airport_position - start_airport_position

