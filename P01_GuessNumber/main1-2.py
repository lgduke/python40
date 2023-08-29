import random
random_number = random.randint(1,100)

print(f"random number:{random_number}")

game_count = 1

while True:
    my_number = int(input("Type the number you guess between 1 to 100 :  "))
    
    if my_number > random_number:
        print("down")
    elif my_number < random_number:
        print("Up")
    elif my_number == random_number:
        print(f"Congraturation. You got answer at {game_count}")
        break
    game_count = game_count+1


        
