# Solution

This crackme was created by eventhorizon02
It is a C program written for x86-64 linux
It has a 2.2 difficulty rating

#### Summary:
	This is a very good crackme for learning how to create keygen. This was the first one that I made my own keygen. It is mostly just looking at code and understanding what conditions are needed to be met to get the final goal.


I used Cutter to analyze the program. I started in the main function and tried to see where the end goal was. This was to get the flag to print. Working backwards you can see that *check_pass* is called and the result determines whether or not you can print the flag. In order to print the flag the return result of *check_pass* has to not be 0.

![check-pass](insertcheckpassimg)

So in order to get the right value we need to analyze the *check_pass* function. The first thing that it does is make a simple check to make sure that a value was supplied as a argument when the code was run. Two, because the first argument is the name of the program and the second being the first supplied argument. Then the length of the provided argument is found by using strlen at 
0x00000811. Then the string is passed to atoi at 0x00000820. Atoi converts a string to a integer. Futher info can be found in the man page or through google. At this point the assembly gets a little rough so i would switch to a decompiler. When then find that the length of the string is being checked to see if it can be %3 and have a remainder of 0. It also checks to see if it is a prime number. One final statement makes it so that the number can't be 0. All of these have to be met or else 0 is returned.

![check](insertcheckimg)

This returns the value that we are looking for, namely not 0, so 1. There is also a *is_prime* function but it just checks to make sure that the number is a prime number.  

Now the next step is to generate a number or numbers that can meet these conditions.
 - %3 == 0
 - is a prime number
 - != 0

For this I created a keygen using python. It is included in the folder. The keygen is loaded with a list of prime numbers ranging from 2, 997. It loops through that list makeing sure that it meets all the conditions that are required. It will then print a final list of numbers that will work.

After the number is generated. Run the file with the number as the argument.

![final-result](insertfinalresult)
