import random
import time
words = ["Python", "Scarce", "Monkey", "Battle", "GitHub"]
choose = random.choice(words).lower() #.lower()converts any string to lowerase.
lifespan = 6
guessed = []
game_over = False

print("Welcome to Hangman!")
time.sleep(2)
print("Get Ready")
time.sleep(2)
while lifespan > 0 and not game_over:
    print(f"Lives remaining: {lifespan}")
    for letter in choose:  #the for loop goes through each letter in the choosen word one by one.
        if letter in guessed: #the for loop checks if that letter has already been guessed
            print(letter, end=" ")  #if yes- show letter
        else:
            print("_", end=" ")   #if no- show _
    print()
    guess = input("Guess a letter: ").lower()  #the way its indented means its under the while loop block and using input() instead of print() is like a two way, it would display the Guess the letter and still allow input from the user unlike print() that just displays.
    if guess in guessed:
        print("you already guessed this letter")
    else:
        guessed.append(guess)
        if guess in choose:
            print("Great job")
            if all(letter in guessed for letter in choose):
                game_over = True
        else:
            lifespan = lifespan - 1
            print("Wrong guess!")
if lifespan == 0: #== compares two values while = assigns a value.
    print("YOU LOST")
else:
    print("CONGRATULATIONS")


