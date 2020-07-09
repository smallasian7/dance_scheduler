"""
Define the class structure for a 'dance class', instructor, and studio
"""

class Dance_class:
    def __init__(self, name, days, duration, instructor, conflicts):
        """
        :param name: string - name of the dance class
        :param days: list of the days of the week that the class may occur
        :param duration: int - duration of the class [minutes]
        :param instructor: string - name of the instructor of the class
        :param conflicts: list of the dance levels that the class cannot be scheduled at the same time
        """
        self.name = name
        self.days = days
        self.duration = duration
        self.instructor = instructor
        self.conflicts = conflicts

class Instructor:
    def __init__(self, name, days):
        """
        :param name: string - instructor name
        :param days: list of the days of the week that the instructor can teach
        """
        self.name = name
        self.days = days

class Studio:
    num_rooms = 4
