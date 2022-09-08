#!/usr/bin/python3

import string

# key NNNN@N-NNlNNNNN? , N being any character

keys = []

# to implement character generation
characters = list(string.ascii_letters)

# generate the keys
num_keys = 50
print(characters)
for i in range(0, len(characters)):
    character = characters[i]
    keys.append(character * 4 + "@" + character + "-" + character * 2 + "l" + character * 5 + "?") 

# print the keys in a neat fashion
spot = 0
for i in range(0, len(keys)):
    print(spot, end="")
    print( ": " + keys[i])
    spot += 1
