import random
number = random.randint(1, 9)
chances = 0
while (chances < 5):
    guess = int(input("enter the number between 1-9 "))
    if (guess > number):
        print("Your guess is larger than you typed")
    elif (guess == number):
        print("Congratulation! You Won")
    else :
        print("Your guess is less than you typed")
    chances = chances + 1
if (chances == 5):
    print("You Lost !! The number is " , number)