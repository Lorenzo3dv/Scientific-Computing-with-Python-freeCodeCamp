def add_time(start, duration, day = ""):
    week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    #list with the 2 times
    times = []
    split_start = start.split()
    times.append(split_start[0])
    times.append(duration)
    
    #list for hours and minutes
    hours = []
    minutes = []
    for time in times:
        splitted_time = time.split(":")
        hours.append(splitted_time[0])
        minutes.append(splitted_time[1])

    #convert to 24h format if PM
    if split_start[1] == "PM":
        hours[0] = str(int(hours[0]) + 12)

    #sum minutes
    sum_minutes = int(minutes[0]) + int(minutes[1])
    final_minutes = sum_minutes
    hours_to_add = 0
    if sum_minutes >= 60:
        hours_to_add = sum_minutes // 60
        final_minutes = sum_minutes % 60

    #sum hours
    sum_hours = int(hours[0]) + int(hours[1]) + hours_to_add
    final_hours = sum_hours
    passed_days = 0
    if sum_hours > 24:
        passed_days = sum_hours // 24
        final_hours = sum_hours - (passed_days * 24)

    #if necessary convert to PM format
    conversion = False
    if final_hours > 12:
        final_hours = final_hours - 12
        conversion = True
        
    #create the string to return
    final_minutes = str(final_minutes)
    final_hours = str(final_hours)
    if len(final_minutes) == 1:
        final_minutes = "0" + final_minutes
    message = ""
    if day in week_days:
        final_day = week_days[week_days.index(day) + passed_days]
        if passed_days == 1:
            message = final_day + " (next day)"
        elif passed_days > 1:
            message = final_day + " (" + str(passed_days) + " days later)"
    else:
        if passed_days == 1:
            message = "(next day)"
        elif passed_days > 1:
            message = "(" + str(passed_days) + " days later)"


    new_time = ""
    if conversion:
        new_time = final_hours + ":" + final_minutes + " PM " + message
    else:
        new_time = final_hours + ":" + final_minutes + " AM " + message

    return new_time