"""
This reverses the string hidden in the binary
it is basically a code rip/black box method way of solving this
"""

# string that was taken from ltrace
userInput = "]\020\024LC\020CNM\024?GL4#&A[(R\020\021?S\021LTR"

# length of the string input
length = len(userInput)

# indexers used
i = length - 1
j = -2


# list to store the converted flag
# the algorthim actually stops at len - 1
# in order to satisfy this we can essentially make an array
splitFlag = [''] * length

# algorthim used in the program
# runs the length of the input
for character in userInput:
    
    # prints are for showing the conversion
    print(character)
    # to reverse the algorthim + 0x20 (32)
    generatedString = chr(ord(character) + 0x20)
    print(generatedString)
    splitFlag[i] = generatedString

    # change the index after -1
    i = i + j
    if i == -1:
        i = 0
        j = 2

# flag joined together
print("".join(splitFlag))
