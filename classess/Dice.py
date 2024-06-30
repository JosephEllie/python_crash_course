from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides
        self.count = 1

    def roll_die(self):
        rand_dice = randint(1, self.sides)
        return rand_dice


my_dice_0 = Die()
my_dice_1 = Die(10)
my_dice_2 = Die(20)

print("Die with 6 sides: ")
for _ in range(10):
    print(my_dice_0.roll_die(), end=" ")

print("\nDie with 10 sides: ")
for _ in range(10):
    print(my_dice_1.roll_die(), end=" ")

print("\nDie with 6 sides: ")
for _ in range(10):
    print(my_dice_2.roll_die(), end=" ")