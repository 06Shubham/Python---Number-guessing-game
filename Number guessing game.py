import random

ram_no = random.randrange(1, 101)

print(ram_no)

chance = 5

while chance > 0:

    inp = int(input("enter your guess: "))

    if inp != ram_no:
        chance -= 1
        print("You have guess the wrong number!!")

    else:
        print("You have guess the correct number!!!")
        print("You have won the game!!!!!!!")
        break

if chance == 0:

    print("You have loos the game!! As you have use your all chances!!")