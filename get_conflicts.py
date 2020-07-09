def get_conflicts(day_schedule, pending_room, time_slot, conflicts):
    conflict_flag = False

    for room in day_schedule:
        if room == pending_room:
            continue
        else:
            for conflict in conflicts:
                if conflict in room[time_slot]:
                    conflict_flag = True
                    return conflict_flag
    else:
        return conflict_flag