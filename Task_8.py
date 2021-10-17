def time_converter(number):
    """This function converts a number to the corresponding value 
    in hours and minutes."""
    hours = number // 60
    minutes = number % 60

    if hours <= 1 and minutes > 1:
        time = f"{hours} hour, {minutes} minutes"
    elif minutes <= 1 and hours > 1:
        time = f"{hours} hours, {minutes} minute"
    elif hours <=1 and minutes <= 1:
        time = f"{hours} hour, {minutes} minute"
    else:
        time = f"{hours} hours, {minutes} minutes"
    return time

print(time_converter(50))