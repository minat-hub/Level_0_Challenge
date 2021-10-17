def convert_to_fahrenheit(celsius):
    """This function converts a value in celsuis degrees to fahrenheit degrees and
    returns the value in fahrenheit."""
    fahrenheit = (9 / 5 * celsius) + 32
    return fahrenheit


def convert_to_celsius(fahrenheit):
    """This function converts a value in fahrenheit degrees to celsuis degrees and
    returns the value in celsuis."""
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


print(convert_to_fahrenheit(20))
print(convert_to_celsius(20))
