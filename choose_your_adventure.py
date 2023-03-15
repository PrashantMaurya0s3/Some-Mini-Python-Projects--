
name = input("Type your name : ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end you can go left or right. "
               "which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to river, you can walk around it or swim across? "
                   "Types walk to walk around and swim to swim across : ")

    if answer == "swim":
        print("You swam across and were eaten by  an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print("Not a valid option. You loose")

elif answer == "right":
    answer = input("you come to bridge, it looks wobbly, "
                   "do you want to cross it or head back? (cross/back) ")
    if answer == "back":
        print("You go back and loose.")
    elif answer == "cross":
        answer = input("You cross the bridge and meet the stranger. Do you want to talk (yes/no)? ")

        if answer == "yes":
            print("You meet the stranger and get the gold. You win!")
        elif answer == "no":
            print("You did not talk to the stranger he offended. you loose!")
        else:
            print("Not a valid option. You loose")

else:
    print("Not a valid option. You loose")

print("Thank you for trying", name)