# Solution
This crackme was created by: RaphDev
It is an x86-64 arch C crackme for linux based systems
It has a rated didiculty of 1.4

Tools: Ghidra

Summary/Info:
 - *Quick note that this crackme was one of the first ones that I orginally did. This was also before I thought about uploading my work and because of this I didn't take good notes. I am doing this based on what notes I have and repiecing it togther. I just thought it would not hurt to upload it for showing progression.*

It was a nice beginner crackme that was pretty simple.

### Analysis:
A decompiler was heavily used in this process since I didn't know assembly at the time.

Examing the *main* function, it appears to be password checker that generates a password. This is done through taking in user input like a username and a number.

These are used to build the password and store it into an array.

![generation](https://github.com/VJMumphrey/Crackme-Writeups/blob/main/PleaseCrackMe/screenshots/generation_pic.png)

When broken down, each index of the array of characters is converted to a number. The number supplied by the user is then added to that number. So *a* would be *b*, and *c* would be *d* ... etc. 

After the key is built, the user is asked to input the password so that it can be checked against the key. 

If they match the success statement prints to the terminal.

![success_statement](https://github.com/VJMumphrey/Crackme-Writeups/blob/main/PleaseCrackMe/screenshots/success_pic.png)

### Keygen:
I created a password generator/keygen for this just for the sake of being able to automatically creating some. *pass_gen.py* is a simple python script that will generate a password that matches the key that is created. *pass_gen.py* is included with this.

