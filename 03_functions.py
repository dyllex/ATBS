"""
basic function
"""
# def statement - defines the function named hello()
def hello():
    # code block - body of the function
    print('Howdy!')
    print('Howdy!!!')
    print('Hello there.')

hello()
hello()
hello()

"""
def statements with parameters
"""
# A parameter is a variable that an argument is stored in when a function is called. 
def hello(name):
    print('Hello ' + name)

# The argument here is 'Alice'
hello('Alice')
# and here, it's 'Bob'
hello('Bob')

"""
Return values and return statements
"""
# Import the random module
import random 
# getAnswer function is defined with answerNumber as its parameter
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'

r = random.randint(1,9)
fortune = getAnswer(r)
print(fortune)

"""
The None Value
"""
# None represents the absence of a value. 
# Useful when you need to store something that won't be confused for a real value in a variable. 
# Python adds return None to the end of any function definiton with no return statement. 
# The return keyword by itself returns None by default

"""
Keyword arguments and print()
"""
# print('Hello', end='')
print('World')
print('cats', 'dogs', 'mice')
# print('cats', 'dogs', 'mice', sep=',')


"""
Local and Global Scope
"""
# Variables that are assigned in a called function exist in the function's global scope.
# Variables assigned outside all functions exist in the global scope. 

# Local scope is created whenever a function is called.
# When the function returns, the local scope is destroyed, and all its variables are forgotten. 

# -- Code in global scope cannot use any local variables -- 
# -- Local scope CAN access global variables -- 
# -- Code in a function's local scope cannot use variables in any other local scope -- 
# -- You can have a global variable and local variable share the same name -- 


"""
Local variables cannot be used in the global scope
"""
def spam():
    eggs = 31337 
# spam ()
# print(eggs)


"""
Local scopes cannot use variables in other local scopes
"""
# A new local scope is created whenever a function is called, including when a function is called from aother function. 
def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0 

spam()


"""
Global variables can be read from a local scope
"""
def spam():
    print(eggs)
eggs = 42
spam()
print(eggs)


"""
Local and global variables with the same name 
"""
# You should avoid using local and global variables with the same name, but it's technically legal to do in Python. 
def spam():
    eggs = 'spam local'
    print(eggs) # prints 'spam local'

def bacon():
    eggs = 'bacon local'
    print(eggs) # prints 'bacon local'
    spam()
    print(eggs) # prints 'bacon local'

eggs = 'global'
bacon()
print(eggs) # prints 'global'


"""
The global statement
"""
# If you need to modify a global variable from within a function, use the global statement. 
# Using the global statement tells Python to not create a local variable with that name. 
def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)

# Rules about global variables 
# 1. If a variable is being used in global scope, then it is always a global variable. 
# 2. If there is a global statement for that variable in a function, it is a global variable. 
# 3. Otherwise, if the variable is used in an assignment statement in the function, it is a local variable. 
# 4. But if that variable is not used in an assignment statement, it is a global variable. 

def spam():
    global eggs
    eggs = 'spam' # this is the global

def bacon():
    eggs = 'bacon' # this is a local 

def ham():
    print(eggs) # this is the global

eggs = 42 # this is the global 
spam()
print(eggs)


"""
Exception handling
"""
# If you don't setup error/exception handling, an error will cause your program to crash.
def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))


"""
A short program: Guess the number
"""
# This is a guess the number game. 
import random 
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times.
for guessesTaken in range(1,7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # This condition is the correct guess
    
if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))


"""
Practice Questions

1. Why are functions advantageous to have in your programs?
# Saves time. Just call function instead of writing the same code. Also keeps code organized. 

2. When does the code in a function execute: when the function is defined or when the function is called? 
# When it's called. 

3. Whate statement creates a function? 
# def statement

4. What is the difference between a function and a function call?
# function is a block of code that operates like a black box. Does not do anything until it is called.  

5. How many global scopes are there in a Python program? How many local scopes? 
# One global scope, local scope for each function. 

6. What happens to variables in a local scope when the function call returns?
# They get deleted. 

7. What is a return value? Can a return value be part of an expression?
# Return value is what the function reports after it finishes. 

8. If a function does not have a return statement, what is the return value of a call to that function?
# Returns False by default. 

9. How can you force a variable in a function to refer to the global variable? 
# Use the keyword 'global' followed by the variable name.

10. What is the data type of None? 
# NoneType data type

11. What does the import areallyourpetsnamederic statement do? 
# Imports all the functions in that .py file. 

12. If you had a function named bacon() in a module named spam, how would you call it after importing spam? 
# spam.bacon()

13. How can you prevent a program from crashing when it gets an error?
# Try and except statements

14. What goes in the try clause? What goes in the except clause?
# Try clause - code with potential error. 
# Except clause - code that is executed if an error occurs in the try clause. 

"""

