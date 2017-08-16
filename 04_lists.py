"""
The list data type
"""
# Lists look like this
# ['cat', 'bat', 'rat', 'elephant']

# The value [] is an empty list that contains no values, similar to '', the empty string.

"""
Getting individual values in a list with indices 
"""
# spam[0] evaluates to the first element stored in the list spam.
# Indices can only be integers and usually start at 0 and go up.

# However, you can also have negative indices. 
# -1 refers to the last index in a list, and -2 refers to the second-to-last index in a list

"""
Getting sublists with slices
"""
# Index gets a single value from a list, but slice can get several values from a list in the form a new list.
# A slice is typed between square brackets, like an index, but it has integers separated by a colon. 

# spam[2] is a list with an index (one integer)
# spam[1:4] is a list with a slice (two integers) 

# In a slice, the first integer is the index where the slice starts. The second integer is the index where the slice ends. The slice goes up to, but does not include, the value at the second index. 
# A slice evaluates to a new list value. 

# As a shortcut, you can omit one or both indices on either side of the colon in a slice. 
# Leaving out the first index is the same as using 0 (beginning of the list)
# Leaving out the second index is the same as using the length of the list, which will slice to the end of the list. 
# spam[:] evaluates to the entire list


"""
Getting a list's length with len()
"""
# len() function returns the number of values that are in a list value passed to it 

"""
Changing values in a list with indices
"""
# spam[1] = 'aardvark' means assign the value at index 1 in the list spam to the string 'aardvark'

"""
List concatenation and list replication 
"""
# You can add lists together with the '+' operator 
# [1, 2, 3] + ['A', 'B', 'C'] results with [1, 2, 3, 'A', 'B', 'C']

"""
Removing values from lists with del statements
"""
# del statement will delete values at an index in a list. 
# del spam[2] deletes the third item in spam

"""
Working with lists
"""
# Don't assign new variables for each piece of data. Don't repeat your code. Use lists!

# catNames = []
# while True:
#     print('Enter the name of cat ' + str(len(catNames) + 1) +
#         ' (Or enter nothing to stop.):')
#     name = str(input())
#     if name == '':
#         break
#     catNames = catNames + [name] # list concatenation

# print('The cat names are:')
# for name in catNames:
#     print(' ' + name)

# use ' ' when typing your answers. Not sure why this is needed. 

"""
Using for loops with lists
"""
for i in range(4):
    print(i)

for i in [0, 1, 2, 3]: 
    print(i)

supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])


"""
The in and not in operators
"""
# Determine whether a value is or isn't in a list with the in and not in operators. 
# Expressions using these operators evaluate to a Boolean value. 

myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name:')
name = input()
if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')


"""
The multiple assignment trick
"""
# This is a lot of typing (so it's bad)
cat = ['fat', 'orange', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2] 

# This approach is more efficient, but the number of variables and length of the list must be exactly equal or you'll get a ValueError
cat = ['fat', 'orange', 'loud']
size, color, disposition = cat


"""
Augmented assignment operators
"""
# spam += 1
# spam = spam + 1

# spam -= 1
# spam = spam - 1

# spam *= 1
# spam = spam * 1

# spam /= 1
# spam = spam / 1

# spam %= 1
# spam = spam % 1


"""
Methods
"""
# A method is the same thing as a function, except it is "called on" a value. 
# E.g. if a list value were stored in spam, you would call the index() list method
# So, spam.index('hello') 

"""
Finding a value in a list with the index() method
"""
# spam = ['cat', 'dog', 'bat']
# spam.index('dog') == 1 

"""
Adding values to lists with the append() and insert() methods
"""
# spam.append('element')
# spam.remove('element')

"""
Sorting the values in a list with the sort() method
"""

"""
Strings can be considered a list of characters
"""
name = 'NEATO!'
for i in name:
    print('* * * ' + i + ' * * *')


"""
Mutable and immutable data types
"""
# Lists are mutable. They can have values added, removed, or changed. 
# Strings are immutable. They cannot be changed. Trying to reassign a single character in a string results with TypeError
# The proper way to 'mutate' a string is to use slicing and concatenation 

"""
The tuple data type
"""
# Tuples are almost like lists, but there are some differences. 
# Tuples are typed with () instead of []
# Tuples are immutable while lists are mutable 
# Tuple with just one value needs a comma inside the () => type(('hello',))

# You can use tuples to convey to anyone reading your code that you don’t intend for that sequence of values to change. If you need an ordered sequence of values that never changes, use a tuple. A second benefit of using tuples instead of lists is that, because they are immutable and their contents don’t change, Python can implement some optimizations that make code using tuples slightly faster than code using lists.

"""
References
"""
# Variables store values separately
# Lists are assigned references. A reference is a value that points to some bit of data, and a list reference is a value that points to a list. 

