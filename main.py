import random # importing random module

def number_guessing_game(): # defining the function
    n = random.randint(1, 100)
    guesses = 0 # initializing the number of guesses

    while True: # looping until the user guesses the correct number
        guesses += 1
        try:
            a = int(input("Enter the number: "))
        except ValueError: # handling the case where the user enters a non-integer value
            print("Invalid input. Please enter a number.")
            continue  # Go back to the beginning of the loop

        if a > n:
            print("Enter a smaller number")
        elif a < n:
            print("Enter a larger number")
        else:
            print(f"You guessed the number in {guesses} guesses")
            break  # Exit the loop when the number is guessed

if __name__ == "__main__": # calling the function
    number_guessing_game()   