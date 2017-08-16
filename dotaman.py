import random
import sys

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

word = words[random.randint(0, len(words)-1)]

print("You have just entered a game of 'Hangman'!! If you don't know how to play, use Google or ask a friend. The game is simple enough, so buckle up and let's start!")
print('')

def game_status(guesses):
    if set(word) == set(guessed):
        print('You guessed it!! Congrats on winning!')
        sys.exit()
    elif guesses == 0:
        print("You're all out of guesses! The correct answer was '%s'." %word)
        print("Better luck next time!!")
        sys.exit()
    elif guesses > 0:
        print("You have %s guesses remaining." %guesses)
        print("Please guess a letter.")

guesses = 6
guessed = [' ', '-', "'"]
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

    
