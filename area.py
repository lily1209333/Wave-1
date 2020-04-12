from math import floor
length = input("print the length in feet: ")
width = input("print the width in feet: ")
l = int(length)
w = int(width)
area = l * w
acres = floor(area/43560)
print(acres, "acres")
