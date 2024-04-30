# Python - Hello, World

## Requirements

### General

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.*)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file at the root of the repo, containing a description of the repository
- A README.md file, at the root of the folder of this project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using wc

## More info

### Pycodestyle

Pycodestyle is now the [new standard of Python style code](https://github.com/PyCQA/pycodestyle/issues/466)

## Tasks

### 0. Hello, print

Write a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.

Use the function print

Example:

```
guillaume@ubuntu:~/py/$ ./2-print.py 
"Programming is like building a multilingual puzzle
guillaume@ubuntu:~/py/$
```

### 1. Print integer

Complete this [source code](https://github.com/hs-hq/0x00.py/blob/main/3-print_number.py) in order to print the integer stored in the variable number, followed by Battery street, followed by a new line.

- You can find the source code here
- The output of the script should be:
    - the number, followed by Battery street,
    - followed by a new line
- You are not allowed to cast the variable number into a string
- Your code must be 3 lines long
- You have to use f-strings tips

Example:

```
guillaume@ubuntu:~/py/0x00$ ./3-print_number.py
98 Battery street
guillaume@ubuntu:~/py/0x00$ 
```

### 2. Print float

Complete the [source code](https://github.com/hs-hq/0x00.py/blob/main/4-print_float.py) in order to print the float stored in the variable number with a precision of 2 digits.

- You can find the source code here
- The output of the program should be:
    - Float:, followed by the float with only 2 digits
    - followed by a new line
- You are not allowed to cast number to string
- You have to use f-strings

```
guillaume@ubuntu:~/py/0x00$ ./4-print_float.py
Float: 3.14
guillaume@ubuntu:~/py/0x00$ 
```

### 3. Print string

Complete this [source code](https://github.com/hs-hq/0x00.py/blob/main/5-print_string.py) in order to print 3 times a string stored in the variable str, followed by its first 9 characters.

- You can find the source code here
- The output of the program should be:
    - 3 times the value of str
    - followed by a new line
    - followed by the 9 first characters of str
    - followed by a new line
- You are not allowed to use any loops or conditional statement
- Your program should be maximum 5 lines long

Example:

```
guillaume@ubuntu:~/py/$ ./5-print_string.py 
Holberton SchoolHolberton SchoolHolberton School
Holberton
guillaume@ubuntu:~/py/$ 
```

### 4. Play with strings

Complete this [source code](https://github.com/hs-hq/0x00.py/blob/main/6-concat.py) to print Welcome to Holberton School!

- You can find the source code here
- You are not allowed to use any loops or conditional statements.
- You have to use the variables str1 and str2 in your new line of code
- Your program should be exactly 5 lines long

Example:

```
guillaume@ubuntu:~/py/$ ./6-concat.py
Welcome to Holberton School!
guillaume@ubuntu:~/py/$ wc -l 6-concat.py
5 6-concat.py
guillaume@ubuntu:~/py/$ 
```

### 5. Copy - Cut - Paste

Complete this [source code](https://github.com/hs-hq/0x00.py/blob/main/7-edges.py)

- You can find the source code here
- You are not allowed to use any loops or conditional statements
- Your program should be exactly 8 lines long
- word_first_3 should contain the first 3 letters of the variable word
- word_last_2 should contain the last 2 letters of the variable word
- middle_word should contain the value of the variable word without the first and last letters

Example:

```
guillaume@ubuntu:~/py/$ ./7-edges.py
First 3 letters: Hol
Last 2 letters: on
Middle word: olberto
guillaume@ubuntu:~/py/$ wc -l 7-edges.py
8 7-edges.py
guillaume@ubuntu:~/py/$ 
```

### 6. Create a new sentence

Complete this [source code](https://github.com/hs-hq/0x00.py/blob/main/8-concat_edges.py) to print object-oriented programming with Python, followed by a new line.

- You can find the source code here
- You are not allowed to use any loops or conditional statements
- Your program should be exactly 5 lines long
- You are not allowed to create new variables
- You are not allowed to use string literals

Example:

```
guillaume@ubuntu:~/py/$ ./8-concat_edges.py
object-oriented programming with Python
guillaume@ubuntu:~/py/$ wc -l 8-concat_edges.py
5 8-concat_edges.py
guillaume@ubuntu:~/py/$ 
```

### 7. Easter Egg

Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.

- Your script should be maximum 98 characters long (please check with wc -m 9-easter_egg.py)

Example:

```
guillaume@ubuntu:~/py/$ ./9-easter_egg.py
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
guillaume@ubuntu:~/py/$
```

### 9. Divide and rule

Write a script that prints the result of POWER divided by DIVIDE, followed by a new line.

- POWER and DIVIDE are environment variables

Example:

```
julien@production-503e7013:~$ export POWER=42784
julien@production-503e7013:~$ export DIVIDE=32
julien@production-503e7013:~$ ./9-divide_and_rule | cat -e
1337$
julien@production-503e7013:~$
```

### 10. Love is anterior to life, posterior to death, initial of creation, and the exponent of breath

Write a script that displays the result of BREATH to the power LOVE

- BREATH and LOVE are environment variables
- The script should display the result, followed by a new line

Example:

```
julien@production-503e7013:~/$ export BREATH=4
julien@production-503e7013:~/$ export LOVE=3
julien@production-503e7013:~/$ ./10-love_exponent_breath
64
julien@production-503e7013:~/$
```

### 11. There are 10 types of people in the world -- Those who understand binary, and those who don't

Write a script that converts a number from base 2 to base 10.

- The number in base 2 is stored in the environment variable BINARY
- The script should display the number in base 10, followed by a new line

Example:

```
julien@production-503e7013:~/$ export BINARY=10100111001
julien@production-503e7013:~/$ ./11-binary_to_decimal
1337
julien@production-503e7013:~/$
```

### 12. Combination

Create a script that prints all possible combinations of two letters, except oo.

- Letters are lower cases, from a to z
- One combination per line
- The output should be alpha ordered, starting with aa
- Do not print oo
- Your script file should contain maximum 64 characters

Example

```
julien@ubuntu:/tmp/0x03$ echo $((26 ** 2 -1))
675
julien@ubuntu:/tmp/0x03$ ./12-combinations | wc -l
675
julien@ubuntu:/tmp/0x03$ 
julien@ubuntu:/tmp/0x03$ ./12-combinations | tail -303 | head -10
oi
oj
ok
ol
om
on
op
oq
or
os
julien@ubuntu:/tmp/0x03$ 
```

### 13. Floats

Write a script that prints a number with two decimal places, followed by a new line.

The number will be stored in the environment variable NUM.

```
ubuntu@ip-172-31-63-244:~/0x03$ export NUM=0
ubuntu@ip-172-31-63-244:~/0x03$ ./13-print_float
0.00
ubuntu@ip-172-31-63-244:~/0x03$ export NUM=98
ubuntu@ip-172-31-63-244:~/0x03$ ./13-print_float
98.00
ubuntu@ip-172-31-63-244:~/0x03$ export NUM=3.14159265359
ubuntu@ip-172-31-63-244:~/0x03$ ./13-print_float
3.14
ubuntu@ip-172-31-63-244:~/0x03$
```

### 14. Decimal to Hexadecimal

Write a script that converts a number from base 10 to base 16.

- The number in base 10 is stored in the environment variable DECIMAL
- The script should display the number in base 16, followed by a new line

```
julien@production-503e7013:~/$ export DECIMAL=16
julien@production-503e7013:~/$ ./14-decimal_to_hexadecimal
10
julien@production-503e7013:~/$ export DECIMAL=1337
julien@production-503e7013:~/$ ./14-decimal_to_hexadecimal | cat -e
539$
julien@production-503e7013:~/$ export DECIMAL=15
julien@production-503e7013:~/$ ./14-decimal_to_hexadecimal | cat -e
f$
julien@production-503e7013:~/$
```
