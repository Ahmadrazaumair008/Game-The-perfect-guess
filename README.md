# Game-The-perfect-guess
A fun number guessing game written in Python. The program generates a random number, and the player has to guess it. The program provides feedback (too high/too low) until the correct number is guessed.
'''
import random # importing random module
n = random.randint(1,100)  # generating random number
a = -1   # initializing a variable
guesses = 0  # initializing a variable

while (a != n):  # while loop
  guesses +=1  # incrementing guesses
  a = int(input("Enter the number: "))
  if(a > n):   # if condition
    print("Enter a smaller number")
  else:
    print("Enter a larger number")

# printing the number of guesses
print("You guessed the number in",guesses,"guesses")  
'''
