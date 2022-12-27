# Solution

### File Info
This was a x64 ELF written in C
The author was lodsb with a difficulty of 2.7

### Strings
 - One does not simply find the flag like this ;)

### Abrivations
The binary was slightly encripted to hide names of functions and objects. To make it easier to read, there are going to be some changes.

functions:
 - *_9ff8a42e_cbd2_481f_9c73_6880f720771f* = *err*
 - *_99adb5ad_c9d1_44ff_84ce_b52782ac7aeb* = *algor*
 - *_a97962fc_d68f_47c5_9221_d17da57166a4* = *final_func*

objects:
 - *_dbf69e5f_8300_41c9_8c80_02a819c56349* = *wrong_input*
 - *_a67bcbe1_4a3e_4c27_a894_ae121b083cac* = *right_input*
 - *_867a0be1_691e_4546_9b6c_020df3bcdc93* = *hiddenString*

### Analysis

Starting at main, there is a check on many arguments there are. If the user didn't supply one then *err* is called. This just prints the the usage statement exits with a status of one. If the user did supply input then the its length is checked to make sure it is even. This is done by *&* the length of the input and *1*. The result should result in *0* for even and *1* for odd. When the input is even *algor* is called with the users input being the argument.

With *algor* a block of memory of on the heap is allocated inorder to return the resulting eventual string. Then the userinput is manipulated and stored in that blockof memory

![algorithim](https://github.com/VJMumphrey/Crackme-Writeups/blob/main/grandfather_clock/screenshots/algor_pic.png)

It is mixing the values in unique order. It does this by starting at the index of one less than the length of user input. It then adds every odd numbers values by adding then decrementing the index by *-2*. Once it hits *-1* the indexer will change to *0* and increment by *2*. This then adds all the evens in order up to index length - 2. It returns the pointer to the memory on the heap.

Back in main the string created on the heap is compared to some data in memory.
If the they match then *final_func* is called with the *right_input*. If anthing is wrong before or after the call to *algor*, *final_func* is called with the *wrong_input*. Both inputs are strings that are manipulated to print out messages. The *wrong_input* prints out,

![wrongInput](https://github.com/VJMumphrey/Crackme-Writeups/blob/main/grandfather_clock/screenshots/wrongInput_pic.png)

Inorder to find out what the result of *right_input* is then the hidden string needs to be found. I did through runnning random inputs through ltrace

![ltrace](https://github.com/VJMumphrey/Crackme-Writeups/blob/main/grandfather_clock/screenshots/ltrace_pic.png)

I took this value and made a decripter. Running a decripter will reverse the stringand get the flag. Passing the flag as an argument provides the success statement.

![rightInput](https://github.com/VJMumphrey/Crackme-Writeups/blob/main/grandfather_clock/screenshots/rightInput_pic.png)

### Decription
Comments are provided in the decripter in order to explain it.
