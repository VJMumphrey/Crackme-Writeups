# Solution
This crackme was created by: BitFriends
It is x86-64 arch assembly crackme for linux 
It is a 1.0 difficulty

Tools: Cutter
This was my first all assembly crackme. It was also pretty easy.

I opened the crackme in cutter and read through some of the code and noticed that there is a comparison being made at 0x00401077. If the comparison returned that the two byte values were the same then it would jump to the correct function.

![cmp-pic](https://github.com/VJMumphrey/Crackme-Writeups/blob/main/nasm_crack/screenshots/cmp_pic.png)

In the *correct_func* you can see that it loads a string called *correct* into RSIfrom 0x00402016. 

![correct-string](https://github.com/VJMumphrey/Crackme-Writeups/blob/main/nasm_crack/screenshots/correct_string.png)

This string looks like two potential outcomes and a password. The full length of the string is 27 characters. This is important for accessing parts of string which seems like its going to happen.

The comparison tests to see if *passwd* and *input* are the same. Input is taken from the user by sys.read while running the program. The *passwd* string is at a specific address in memory (0x00402026). This is in the *correct* string from earlier. The start of the *correct* string is at 0x00402016 and the *passwd* is at 0x00402026. There is 16 bytes between those two (10 base10 is 16 base16) so the password to the program is 16 characters into the *correct* string.

![correct-string](https://github.com/VJMumphrey/Crackme-Writeups/blob/main/nasm_crack/screenshots/correct_string.png)

This would point to *supersecret* to being the password. The comparison from earlier tested if the user input matched the *passwd*.

![final-result](https://github.com/VJMumphrey/Crackme-Writeups/blob/main/nasm_crack/screenshots/final_result.png)

###Easy Way
You could alse just run strings on the file and get,
Enter your password: 
Correct!
Wrong!
supersecret

Then run the program with *supersecret*, but it doesn't help if your are trying to learn. 
