def assign_class(schedule, day, room, name, time_slot, num_time_slots):
    for slots in range(num_time_slots):
        schedule[day][room][time_slot+slots] = name
    return schedule
