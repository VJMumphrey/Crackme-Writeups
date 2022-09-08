# Solution
This crackme was created by: yariza
It is x86-64 arch C crackme for linux
It has a difficulty of 2.2 

Tools: Cutter
 Summary:  This crackme was a simple to solve. Creating a keygen for it wasn't to difficult either.

### Analysis:
Starting out in *main*, there isn't a whole bunch going on. There was a check to make sure that a key was passed in and that was it.

If the condition was met then the key was passed into *check_pw*. In *check_pw* there are checks to see if certain characters are in the correct spots.

![checks-pic](https://github.com/VJMumphrey/Crackme-Writeups/blob/main/Keygen_Me/screenshots/checks_pic.png)

This process was repeated several times with different character values and spots in the key.
If the checks were met then the success message was printed and a spinning doughnut appeared.

![doughnut](https://github.com/VJMumphrey/Crackme-Writeups/blob/main/Keygen_Me/screenshots/doughnut.png)

Now that the algorithim is solved, the next step is to create a keygen to generate the keys.

### Keygen:
I created a keygen named *keygen.py* which is included.
In order to generate the keys there are certain conditions that have to be met.

- the 0x4 position has to be a *@* symbol
- the 0x6 position has to be a *-* symbol
- the 0x9 position has to be a "l" character
- the 0xf position has to be a *?* symbol

this could look something like this,
NNNN@N-NNlNNNNN? , with N being any character

*keygen.py* is explained in the file.

