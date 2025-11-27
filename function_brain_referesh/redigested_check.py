def check_minutes(minutes):
    seconds = minutes * 60
    hours = minutes / 60
    time = (f'{minutes} minutes is {seconds} seconds {hours} hours')
    return time

print(check_minutes(30))

