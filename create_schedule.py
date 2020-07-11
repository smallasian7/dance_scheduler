# from classes import Dance_class
# from classes import Instructor
# from classes import Studio
import json
import math
from get_conflicts import get_conflicts
from assign_class import assign_class

TIME_SLOT_DUR = 30      # Minutes
NUM_TIME_SLOTS = 6      # Number of time slots available to schedule
NUM_ROOMS = 4           # Number of rooms
ROOM_LIST = ['room 1', 'room 2', 'room 3', 'room 4']    # List of room names in order
unscheduled_list = []   # List of classes that could not be scheduled

# Each 'None' element is a 30 minute segment
# Only considering scheduling group dances between 1700-2000
schedule = {
    "monday": {
        "room 1": [None, None, None, None, None, None],
        "room 2": [None, None, None, None, None, None],
        "room 3": [None, None, None, None, None, None],
        "room 4": [None, None, None, None, None, None]
    },
    "tuesday": {
        "room 1": [None, None, None, None, None, None],
        "room 2": [None, None, None, None, None, None],
        "room 3": [None, None, None, None, None, None],
        "room 4": [None, None, None, None, None, None]
    },
    "wednesday": {
        "room 1": [None, None, None, None, None, None],
        "room 2": [None, None, None, None, None, None],
        "room 3": [None, None, None, None, None, None],
        "room 4": [None, None, None, None, None, None]
    },
    "thursday": {
        "room 1": [None, None, None, None, None, None],
        "room 2": [None, None, None, None, None, None],
        "room 3": [None, None, None, None, None, None],
        "room 4": [None, None, None, None, None, None]
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
        day = 0

        while day < num_days and not scheduled_flag:
            room = 0
            while room < NUM_ROOMS and not scheduled_flag:
                for time_slot in range(NUM_TIME_SLOTS):
                    temp_day = days[day]
                    temp_room = ROOM_LIST[room]
                    if schedule[temp_day][temp_room][time_slot] is None:
                        # Find conflicts
                        conflict_flag = get_conflicts(schedule[temp_day], temp_room, time_slot, conflicts)
                        # If no conflicts
                        if not conflict_flag:
                            # Assign to room
                            num_time_slots_req = math.ceil(duration/TIME_SLOT_DUR)
                            schedule = assign_class(schedule, temp_day, temp_room, name, time_slot, num_time_slots_req)
                            scheduled_flag = True
                            break
                room += 1
            day += 1
        if not scheduled_flag:  # If dance class was not scheduled
            unscheduled_list.append(name)

    json = json.dumps(schedule)
    file_write = open("completed_schedule.json", "w")
    file_write.write(json)
    file_write.close()

print(unscheduled_list)
file.close()
