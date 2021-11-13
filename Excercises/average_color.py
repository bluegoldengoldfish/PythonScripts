# Calculate the average color of given two hexadecimal strings
# Average color is calculated by the arithmetic mean of each color component

import math


def average_color(color1, color2):
    # is assumed that the arguments are passed in as an hex formatted string i.e. 123BDF

    red = math.trunc(
        (int(color1[0:2], 16) + int(color2[0:2], 16)) / 2)
    green = math.trunc(
        (int(color1[2:4], 16) + int(color2[2:4], 16)) / 2)
    blue = math.trunc(
        (int(color1[4:6], 16) + int(color2[4:6], 16)) / 2)

    return str(hex(red)).upper()[2:] + str(hex(green)).upper()[2:] + str(hex(blue)).upper()[2:]


# Main method.
if __name__ == '__main__':
    average_color('123BDF', '645AAA')

