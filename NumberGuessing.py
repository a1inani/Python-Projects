import random
def number_guessing():
    """Make a program which randomly chooses a number to guess and then the user will have a few chances 
    to guess the number correctly. In each wrong attempt, the computer will give a hint that the number 
    is greater or smaller than the one you have guessed.
    """
    #Select a random number between 1 and 100
    rand_num = random.randint(1, 101)
    #Repeat the following snippet until a break statement is reached
    while True:
        try:
            #Exception handling. Get the input and try casting it to int
            guess = int(input("Guess the number: "))
            if guess == rand_num:
                print("Correct!")
                break
            elif guess > rand_num:
                print("Too high. Guess again.")
            elif guess < rand_num:
                print("Too low. Guess again.")
        except (NameError):
            #Throw error if input is not a number
            print("This is not a valid number.")
        

if __name__ == "__main__":
    number_guessing()