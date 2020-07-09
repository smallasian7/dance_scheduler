# from classes import Dance_class
# from classes import Instructor
# from classes import Studio
import json
import math
from get_conflicts import get_conflicts
from assign_class import assign_class

TIME_SLOT_DUR = 30      # minutes
NUM_ROOMS = 4           # Number of rooms
unscheduled_list = []   # List of classes that could not be scheduled

# Each 'None' element is a 30 minute segment
# Only considering scheduling group dances between 1700-2000
schedule = {
    "monday": {
        "room 1": [None,None,None,None,None,None],
        "room 2": [None,None,None,None,None,None],
        "room 3": [None,None,None,None,None,None],
        "room 4": [None,None,None,None,None,None]
    },
    "tuesday": {
        "room 1": [None,None,None,None,None,None],
        "room 2": [None,None,None,None,None,None],
        "room 3": [None,None,None,None,None,None],
        "room 4": [None,None,None,None,None,None]
    },
    "wednesday": {
        "room 1": [None,None,None,None,None,None],
        "room 2": [None,None,None,None,None,None],
        "room 3": [None,None,None,None,None,None],
        "room 4": [None,None,None,None,None,None]
    },
    "thursday": {
        "room 1": [None,None,None,None,None,None],
        "room 2": [None,None,None,None,None,None],
        "room 3": [None,None,None,None,None,None],
        "room 4": [None,None,None,None,None,None]
    }
}

with open('class_list.json') as file:
    class_list = json.load(file)
    num_classes = len(class_list)

    for item in class_list:
        # Get class info
        name = item['name']
        instructor = item['instructor']
        days = item['days']
        duration = item['duration']
        conflicts = item['conflicts']

        # Boolean to determine whether the dance class has been successfully scheduled
        scheduled_flag = False

        num_days = len(days)
        num_rooms =

        while day in days and not scheduled_flag:
            for room in schedule[day]:
                for time_slot in range(len(room)):
                    if schedule[day][room][time_slot] is None:
                        # Find conflicts
                        conflict_flag = get_conflicts(schedule[day], room, time_slot, conflicts)
                        # If no conflicts
                        if not conflict_flag:
                            # Assign to room
                            num_time_slots = math.ceil(duration/TIME_SLOT_DUR)
                            schedule = assign_class(schedule, day, room, name, time_slot, num_time_slots)
                            scheduled_flag = True
                            break
        else:
            unscheduled_list.append(name)

    json = json.dumps(schedule)
    file_write = open("completed_schedule.json","w")
    file_write.write(json)
    file_write.close()

file.close()
