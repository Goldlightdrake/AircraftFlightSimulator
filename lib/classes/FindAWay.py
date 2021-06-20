from lib.classes.Vector import Vector


class FindAWay:
    """
        FindAWay class made for calculating the flight path of the plane:
        - goal airport position (the final flight station of the aircraft)
        - start airport position (starting flight station of the aircraft)
        example init:
        >>> FindAWay(3,5)
        """

    @staticmethod
    def calculate_path(goal_airport_position, start_airport_position):
        if goal_airport_position == start_airport_position:
            return 0
        return goal_airport_position - start_airport_position
