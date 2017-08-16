import random

words = ['cat', 'dog', 'teacher', 'medicine', 'explorer', 'prestige', 'museum', 'mountain', 'hurricane', 'cyclone', 'rain', 'car', 'turtle', 'space', 'universe', 'meteor', 'spiderman']

word = words[random.randint(0, len(words)-1)]

print("You have just entered a game of 'Hangman'!! If you don't know how to play, use Google or ask a friend. The game is simple enough, so buckle up and let's start!")
print('')

def game_status(guesses):
    if set(word) == set(guessed):
        print('You guessed it!! Congrats on winning!')
    elif guesses == 0:
        print("You're all out of guesses! The correct answer was '%s'." %word)
        print("Better luck next time!!")
    elif guesses > 0:
        print("You have %s guesses remaining." %guesses)
        print("Please guess a letter.")

guesses = 6
guessed = []
while guesses >= 0:
    game_status(guesses)
    if guesses == 0:
        break
    guess = input()
    if guess in word:
        guesses += 1
        guessed.append(guess)
    for char in word:
        if char in guessed:
            print('[%s]' %char.upper(), end='')
        else:
            print(' __ ', end='')
    guesses -= 1
    print('')

    
