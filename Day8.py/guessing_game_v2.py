import random
#i remember i use this in previous class i dont know know how this actully works but i 
# rmemebr the syntax how it import random munber form 1 to 100 let the python
#  select the random number and store it in the variable secret
secret = random.randint(1, 5)

print("Guess the number between 1 and 5")
attempts = 0
while True:
    guess = int(input("Guess: "))
    attempts += 1

    if guess < secret:
        print("Too low! Try again.")
    elif guess > secret:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the number.")
        print(f"It took you {attempts} attempts.")
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == "yes" :
            attempts = 0
            secret = random.randint(1, 5)
            print("Guess the number between 1 and 5")
        else:
            print("Thank you for playing!")    
            break