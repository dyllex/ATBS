import random
import sys

# Initialize global variables
guesses = 6
guessed = [' ', '-', "'"]
streak = 1
word = 'example'
# List of all Dota 2 heroes
words = [
    'abaddon',
    'alchemist', 
    'ancient apparition', 
    'anti-mage', 
    'arc warden', 
    'axe', 
    'bane', 
    'batrider', 
    'beastmaster', 
    'bloodseeker', 
    'bounty hunter', 
    'brewmaster', 
    'bristleback', 
    'broodmother', 
    'centaur warrunner', 
    'chaos knight', 
    'chen', 
    'clinkz', 
    'clockwerk', 
    'crystal maiden', 
    'dark seer', 
    'dazzle', 
    'death prophet', 
    'disruptor', 
    'doom', 
    'dragon knight', 
    'drow ranger', 
    'earth spirit', 
    'earthshaker', 
    'elder titan', 
    'ember spirit', 
    'enchantress', 
    'enigma', 
    'faceless void', 
    'gyrocopter', 
    'huskar', 
    'invoker', 
    'io', 
    'jakiro', 
    'juggernaut', 
    'keeper of the light', 
    'kunkka', 
    'legion commander', 
    'leshrac', 
    'lich', 
    'lifestealer', 
    'lina', 
    'lion', 
    'lone druid', 
    'luna', 
    'lycan', 
    'magnus', 
    'medusa', 
    'meepo', 
    'mirana',
    'moneky king',
    'morphling', 
    'naga siren', 
    "nature's prophet",
    'necrophos',
    'night stalker', 
    'nyx assassin', 
    'ogre magi',
    'omniknight',
    'oracle',
    'outworld devourer',
    'phatom assassin', 
    'phantom lancer', 
    'phoenix', 
    'puck', 
    'pudge', 
    'pugna', 
    'queen of pain', 
    'razor', 
    'riki', 
    'rubick', 
    'sand king', 
    'shadow demon', 
    'shadow fiend', 
    'shadow shaman', 
    'silencer', 
    'skywrath mage', 
    'slardar', 
    'slark', 
    'sniper', 
    'spectre', 
    'spirit breaker', 
    'storm spirit', 
    'sven', 
    'techies', 
    'templar assassin', 
    'terrorblade', 
    'tidehunter', 
    'timbersaw', 
    'tinker',
    'tiny', 
    'treant protector', 
    'troll warlord', 
    'tusk', 
    'underlord', 
    'undying', 
    'ursa', 
    'vengeful spirit', 
    'venomancer', 
    'viper', 
    'visage',
    'warlock', 
    'weaver', 
    'windranger', 
    'winter wyvern', 
    'witch doctor', 
    'wraith king', 
    'zeus'
    ]

print("You have just entered a game of 'Dotaman'!! It's just like 'Hangman' but with Dota 2 heroes! If you don't know how to play 'Hangman', use Google or ask a friend. The game is simple enough, so buckle up and let's start!")
print('')
print("You have %s guesses remaining." %guesses)
print("Please guess a letter.")

def new_word():
    global word
    word = words[random.randint(0, len(words)-1)]
    words.remove(word)
    for char in word:
        if char not in [' ', '-', "'"]:
            print(' __ ', end='')
        else:
            print(' %s ' %char, end='')
    print('')
    return word

def game_manager(guesses):
    global streak
    if guesses == 999:
        killstreak(streak)
        streak += 1
        dotaman()
    elif guesses == 0:
        print("You're all out of guesses! The correct answer was '%s'." %word)
        print("Better luck next time!! You guessed %s heroes correctly!" %streak)
        sys.exit()
    elif guesses > 0:
        print("You have %s guesses remaining." %guesses)
        print("Please guess a letter.")
    

def dotaman():
    global streak
    new_word()
    guesses = 6
    guessed = [' ', '-', "'"]
    while True:
        guess = input()
        count = 0
        if guess in word:
            guesses += 1
            guessed.append(guess)
        for char in word:
            if char in guessed:
                print(' %s ' %char.upper(), end='')
                count += 1
                if count == len(word):
                    guesses = 1000
            else:
                print(' __ ', end='')
        guesses -= 1
        print('')
        game_manager(guesses)

def killstreak(streak):
    if streak == 1:
        print ('First blood!!')
    elif streak == 2:
        print('Double kill!')
    elif streak == 3:
        print('Killing spree!!')
    elif streak == 4:
        print("You are dominating!!")
    elif streak == 5:
        print('Megakill~!')
    elif streak == 6:
        print('Unstoppable!!')
    elif streak == 7:
        print('Wicked sick!')
    elif streak == 8:
        print('M-M-M-Monster kill!!')
    elif streak == 9:
        print('GODLIKE!')
    elif streak >= 10:
        print('BEYOND GODLIKE!!')

    print('Now guess the next hero! Only %s remaining!' %len(words))
    print('')
    print('')
    
    if len(words) == 0:
        print('HOLY SHIT! You beat the entire game! You are a Dotaman Master! <3')

# Initialize game
dotaman()


sys.exit()

# Next features
# 1. game repeats, removes name from list
# 2. Keep track of streaks like secret shop quiz