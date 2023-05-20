# Solution

Overall a good starter crackme. I did this as a "warmup" sDince I haven't done much reversing as of late.

### File Info

This file is a x86-64 ELF, not stripped

### Analysis

There is a number is what is being compared at runtime. This number is converted later into a array of chars and compared.

![image](https://github.com/VJMumphrey/Crackme-Writeups/blob/main/trycrackme/screenshots/ans.png)

User input is taken in and being compared to a string made at runtime. 

![image](https://github.com/VJMumphrey/Crackme-Writeups/blob/main/trycrackme/screenshots/comp.png)

This is done with a for loop that takes the byte in the index of the string and then adds it to the new string.

![image](https://github.com/VJMumphrey/Crackme-Writeups/blob/main/trycrackme/screenshots/loop.png)

Inputing the number, and trying out this guess results in success

![image](https://github.com/VJMumphrey/Crackme-Writeups/blob/main/trycrackme/screenshots/success.png)

