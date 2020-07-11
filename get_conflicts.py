def get_conflicts(day_schedule, pending_room, time_slot, conflicts):
    conflict_flag = False

    for room in day_schedule:
        if room == pending_room:
            continue
        else:
            for conflict in conflicts:
                conflict_name = day_schedule[room][time_slot]
                if conflict_name is None:
                    return conflict_flag
                elif conflict in conflict_name:
                    conflict_flag = True
                    return conflict_flag
    else:
        return conflict_flag
