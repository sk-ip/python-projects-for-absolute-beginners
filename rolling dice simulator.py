#
#                            Rolling dice simulator
#
# this is simple program in which the user has to provide the minimum
# and the maximum number for the dice which has n sides. the computer
# the computer will automatically roll the dice and give the number which
# shows up.
#
#

from random import randint

print("************rolling dice simulator****************")
x = int(input("minimum number: "))
y = int(input("maximum number: "))
print("number that showed up:", randint(x, y))
