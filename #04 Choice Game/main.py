name = input("What is your name? ")

print(f"Welcome to the choice game {name}")

while True:
    direction = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

    if direction == "left":
        while True:
            left = input("You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim across: ")

            if left == "walk":
                print("You walked for many miles, ran out of water, and you lost the game.")
                break

            elif left == "swim":
                print("You swam across and were eaten by an alligator.")
                break  
        break

    elif direction == "right":
        while True:
            right = input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")

            if right == "back":
                print("You go back and lose.")
                break

            elif right == "cross":
                while True:
                    cross = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")

                    if cross == "yes":
                        print("You talk to the stanger and they give you gold. You WIN!")
                        break

                    elif cross == "no":
                        print("You ignore the stranger and they are so offended that they killed you.")
                        break
            break
            
        break

print(f"Thanks for playing {name}")




