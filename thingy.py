"""Generate Random Number."""
from random import randint


dice_roll = input("nds: ")
split_array = dice_roll.lower().replace(" ", "").split("d")

while len(split_array) != 2:
    print("Incorrect input, should input number of die, \"d\","
          " then side number. i.e. 1d4")
    dice_roll = input("nds: ")
    split_array = dice_roll.lower().replace(" ", "").split("d")
else:
    die = int(split_array[0])
    sides = split_array[1]

    total = 0

    for dice in range(0, die):
        rand_num = randint(1, int(sides))
        print(str(rand_num))
        total += rand_num

    print("sum: %i" % total)
