import random
from collections import Counter

# List of fruit words for the Hangman game
someWords = '''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''

someWords = someWords.split(' ')
word = random.choice(someWords)

print('Guess the word! HINT: word is a name of a fruit')

# Display initial underscores for the word
for _ in word:
    print('_', end=' ')
print()

playing = True
letterGuessed = ''
chances = len(word) + 2
correct = 0
flag = 0

try:
    while (chances > 0) and flag == 0:  # Flag is updated when the word is correctly guessed
        print()
        chances -= 1

        try:
            guess = str(input('Enter a letter to guess: ')).lower()
        except:
            print('Enter only a letter!')
            continue

        # Validation of the guess
        if not guess.isalpha():
            print('Enter only a LETTER')
            continue
        elif len(guess) > 1:
            print('Enter only a SINGLE letter')
            continue
        elif guess in letterGuessed:
            print('You have already guessed that letter')
            continue

        # If letter is guessed correctly
        if guess in word:
            letterGuessed += guess

        # Display the current state of the word
        correct = 0
        for char in word:
            if char in letterGuessed:
                print(char, end=' ')
                correct += 1
            else:
                print('_', end=' ')

        # Check if the user has guessed all letters
        if correct == len(word):
            flag = 1
            print("\nCongratulations, You won!")
            print("The word is:", word)
            break

    # If user has used all their chances
    if chances <= 0 and correct != len(word):
        print("\nYou lost! Try again.")
        print("The word was:", word)

except KeyboardInterrupt:
    print("\nBye! Try again.")
    exit()
