"""
The Collatz Sequence
"""

def collatz(number):
    if number % 2 == 0:
        return number // 2
    
    elif number % 2 == 1:
        return 3 * number + 1

print("Enter a number:")
number = int(input())

while number != 1:
    number = collatz(number)
    print(int(collatz(number)))