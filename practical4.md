---
layout: page
title: Practical 4
permalink: /practical4/
---

# Objectives

The learning objectives for this practical are:

 * Run your first Python program from the Unix shell.
 * Read data from the keyboard into a Python program.
 * Implement in Python several programs doing basic arithmetic.
 * Implement in Python a program to decide if a natural number is perfect.
 * Make syntax errors in Python.
 * Correct syntax errors in Python.
 * How to debug your program by watching variables.

For the problems in which you have to implement a program that
solves some arithmetic problem that we have solved in class at the
blackboard, you should have already one working solution from that class
on paper. If you don't, please ask a colleague for one. Try
to focus the time of this practical in addressing the technical challenges
of running a Python program and correcting run-time errors.

Whenever you are stuck with an error, please consult the last section
entitled "Debugging".

# Setup and background

To do this practical you need an installation of Python version 3. You can find
the instructions in the [setup](/setup/) link on how to install Python version 3
in your system. Once Python is installed, you should be able to call it from
the shell in the terminal window. You can check whether that is possible by typing:

```
$ which python
$ python --version
```

It may happen that you have two Python installations, one corresponding
to version 2.x and another to version 3.x. In that situation the previous command
may say that your Python version is 2.x and to access the version 3 you need to call
the executable `python3`. Try then for instance:

```
$ python3 --version
```

If this is your case, then whenever the executable `python` is invoked in the rest of
this practical, please use `python3` instead.

# Running Python interactively

The Python executable (`python` or `python3`) that at this point you can run from
the Unix shell can either work interactively or by giving a text file with a
Python program to be executed. In either case, it works as a programming
language
[interpreter](https://en.wikipedia.org/wiki/Interpreter_%28computing%29) rather
than a
[compiler](https://en.wikipedia.org/wiki/Compiler), which means that it will
directly execute the Python instructions you give to it. Among other things, this
means that Python can be run
[interactively](https://en.wikipedia.org/wiki/Interactivity).
To run Python interactively just type `python` on the Unix shell and you should
get an output similar to this one:

```
$ python
Python 3.6.8 (default, Aug  7 2019, 17:28:10) 
[GCC 4.8.5 20150623 (Red Hat 4.8.5-39)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```
The first three lines above are a message about the version of Python and other
system components and the three symbols at the end (`>>>`) are the Python
[command prompt](https://en.wikipedia.org/wiki/Command-line_interface#Command_prompt)
that indicate that the Python interpreter is ready to accept input. Try, for instance,
to type some arithmetic operation such as:

```
>>> 1 + 1
```
Now try to execute the following Python `print()` instruction, which should print
the message `Hello World!` below that instruction.

```
>>> print("Hello World!")
```
An interesting exercise to do from the Python interpreter is to see how Python
identifies different types of values with the function `type()`:

```
>>> type(1)
<class 'int'>
```
Here Python is telling as the the number `1` is of _class_ `int`, which is a
shorthand for _integer_. Let's try some different types of values:

```
>>> type("Hello World!")
<class 'str'>
>>> type(3.14)
<class 'float'>
>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>
```
Here `str` refers to a
[_string of characters_](https://en.wikipedia.org/wiki/String_%28computer_science%29)
`float` to a
[_floating-point number_](https://en.wikipedia.org/wiki/Floating-point_arithmetic)
and `bool` to a
[_boolean data type_](https://en.wikipedia.org/wiki/Boolean_data_type). These are
part of the so-called _Python built-in data types_. If you have a variable `x` for
which you don't know what kind of data type is storing, you can find it out with
a call to the function type, for instance:

```
>>> x = 10
>>> type(x)
<class 'int'>
>>> y = x > 5
>>> type(y)
<class 'bool'>
```

To quit the Python interactive interpreter you can either press `Ctrl+d` or type:

```
>>> quit()
```
As you have just seen, in the Python interactive interpreter you can type any
Python instruction and it will be immediately and interactively executed.
However, this is not the usual way to execute Python programs that consist of
several lines. In general, you want to execute Python programs by writing them
in text files with filename extension `.py` and running them from the Unix shell
as described in the following section, which is also the way in which we will
work throughout the rest of this practical.

# Run your first Python program from the Unix shell

Make a directory for this practical, called `practical4`. Open a text editor, starting
a new empty text file called file called `hello.py`, which should be stored within
the directory `practical4`. Inside this empty file `hello.py`, please write the following
line:

```
print("Hello World!")
```

Make sure this text file is stored within your directory `practical4` by typing the
Unix list command within that directory and verifying that the file `hello.py` is
right there:

```
$ ls
hello.py
```

Once you have your file stored with the previous `print()` line, make sure the file contains
exactly what you have typed in the text editor by exploring its contents with the
Unix `cat` command:

```
$ cat hello.py
print("Hello World!")
```

If the contents are different, then probably you have not saved what you typed in the
text editor. Go to the text editor and save the file. Once we have typed this Python
one-liner program, saved it and made sure the file is in your CWD, containing the expected
source code, you can run it by calling the command `python` with the filename of the
program as argument:

```
$ python hello.py 
Hello World!
```
We should be getting the message "Hello World!" on the terminal window.

# Read data from the keyboard into a Python program.

Most computer programs read some input, make some calculations and write some
output. For each of these three tasks we should use some specific Python
instructions. In the case of reading input from the keyboard, we can use the
function `input()` to which we give one argument with some text we want to
display on screen and it will return whatever we type on the keyboard
**as a character string**. For instance, create a new Python program called
`inputoutput.py` with the following contents:

```
x = input("Enter a value: ")
print(x)
```

Store it on disk and call it from the command line by doing:

```
$ python inputoutput.py
```

The program will ask you to enter a value. Enter any value, for instance a numerical
value 10, or a character string "hello" (without the quotes), and press the `Enter`
key. If you have been able to run this without an error, think about what has happened.
Look at the source code. Try to understand how the value you typed came back on the
terminal window.

# Adding two numbers

Here we are going to implement a Python program that reads two numbers from the keyboard,
adds them and prints the result on the terminal window. Open a new file in the text
editor called `add.py` and type the following code:

```
x = input("Enter one value: ")
y = input("Enter another value: ")
z = int(x) + int(y)
print(z)
```

Execute `add.py` in the terminal window, enter two integer numbers and check out that it
is correctly adding them up. In this program we have used the function `int()` over each
of the variables that read the input numbers because, by default, the function `input()`
returns a character string and applying the addition operator `+` over two character
strings leads to their concatenation, instead of the arithmetic operation we want to do.
The function `int()` coerces a character string of a number into its corresponding
numeric-type value.

Now replace the last line with the call to the `print()` function, by this other
one and save and execute the program again:

```
print("The sum of %s and %s is %d" %(x, y, z))
```

You should obtain an output of the form:

```
The sum of 3 and 4 is 7
```

In this new call to the `print()` function the character string
`"The sum of %s and %s is %d"` is a so-called
[format string](https://en.wikipedia.org/wiki/Printf_format_string), where
symbols `%s` and `%d` are _format specifiers_, which are nothing else than
placeholders for values that we want to insert within the string. Those
values are specified right after the format string, in this example, as
`%(x, y, z)`, where `x`, `y` and `z` are variables whose content is in
one-to-one correspondence with the format specifiers. For this reason,
because `x` and `y` contain character strings, the first two format
specifiers are `%s`, while the third one is `%d` because the value in
variable `z` is a numerical integer value.

Now copy the file of this program `add.py` into another file called `mean.py`. Open
`mean.py` with the text editor and modify the code to provide the calculation of the
arithmetic mean of two values.

# Even and odd numbers

Implement a program in Python that asks for a positive integer number and prints
a message saying whether the number is even or odd.

# Factorial of an integer number.

Implement a program in Python that asks for an integer number and calculates its
[factorial](https://en.wikipedia.org/wiki/Factorial) product.

# Calculation of a base raised to a power.

Implement a program in Python that asks for two numbers, a positive integer number,
which will be the base, and a non-negative integer number, which will be the power,
and calculates the [base raised to the power](https://en.wikipedia.org/wiki/Exponentiation).

# Perfect numbers 

The Wikipedia [page](https://en.wikipedia.org/wiki/Perfect_number) for perfect numbers
says:

> In number theory, a perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. For instance, 6 has divisors 1, 2 and 3 (excluding itself), and 1 + 2 + 3 = 6, so 6 is a perfect number.

Implement a program in Python that asks for a positive integer number and says whether
the given number is perfect or not providing some message with the `print()` function. 

# Debugging

[Debugging](https://en.wikipedia.org/wiki/Debugging) is the process of finding and correcting
bugs in computer programs. A [bug](https://en.wikipedia.org/wiki/Software_bug) in this context
is an unintended error in a computer program that produces an incorrect or unexpected result.
Bugs can be caused by as little as a single letter causing a syntax error. This was the case,
for instance, in 1988 of the failed mission to Mars by the
[Phobos 1](https://en.wikipedia.org/wiki/Phobos_1) space probe, which lost communication with
ground control by a missing hyphen (`-`) in one of the commands that was unintentionally left
out by a technician (remember this guy next time you think you had a bad day in front of the
computer).

Debugging can be time consuming but the more you debug, the faster you do it. It is a kind
of detective task, so pay attention to the clues that Python will give you when printing
error messages, **read them carefully**. Here we illustrate how to start debugging your
Python programs.

## A straightforward syntax error

Let's say that in the first line of the `add.py` Python program we forget closing the
double quotes of the character string:

```
x = input("Enter one value: )
```

This will cause the following syntax error:

```
$ python add.py 
  File "add.py", line 1
    x = input("Enter one value: )
                                ^
SyntaxError: EOL while scanning string literal
```

Note that in the first line of the message, Python is telling us the name of the
file and the line in this file that _Python thinks_ that it contains the syntax error.
Then, that line is printed and underneath, a caret character (`^`) indicates the place
where _Python thinks_ the error takes place. Below that printed line, Python provides
the type of error that is taking place:

```
SyntaxError: EOL while scanning string literal
```
Here, EOL means _end of line_ and the message suggests that while reading the string
literal that started with double quotes, it found the end of line before finding the
closing pair of double quotes.

## A cryptic syntax error

An error slightly more dificult to identify occurs if in the Python program
`add.py` we remove the last character `)` from the third line:

```
z = int(x) + int(y
```

Because when we run the program, we get the following message:

```
$ python add.py 
  File "add.py", line 4
    print("The sum of %s and %s is %d" %(x, y, z))
    ^
SyntaxError: invalid syntax
```
Python thinks that the error is in the fourth line and shows it to us, but that line
is perfect. When this happens, you should always suspect that the problem lies in the
previous line, as it happens here.

## Watching variables

If we execute a Python program and it does not give any error but it also
does not end, we shoud suspect that it has become trapped in an infinite loop.
An infinite loop occurs when in a loop statement the end condition is never met,
that is, the condition that the loop evaluates at each iteration is always true
in the case, for instance, of a `while` loop. In that kind of situation you should
first interrupt the execution of the program by typing the key combination
`Ctrl+c` on the shell where the program is running. Once you have recovered the
control of the shell, then you should modify your program to watch the contents
of the variables that you think might be more relevant to the problem.

For instance, consider the following program that add up the first ten natural
numbers:

```
x = int(input("Enter one value: "))
s = 0
i = 1
while (i <= x) :
    s = s + i
    i = i + 1

print(s)
```

Now, let's say we unintentionally leave the instruction that increases the variable
`i` outside the loop statement:

```
x = int(input("Enter one value: "))
s = 0
i = 1
while (i <= x) :
    s = s + i

i = i + 1

print(s)
```

This will cause an infinite loop but we might not understand why this is happening.
One way to find it out is to watch the contents of variables during looping. We can
do that by adding printing statements of the variables, for instance:

```
x = int(input("Enter one value: "))
s = 0
i = 1
while (i <= x) :
    print("i=%d s=%d" %(i, s))
    s = s + i

i = i + 1

print(s)
```
When we execute this program we will see the following output going on and on
indefinitely through our terminal window:

```
i=1 s=0
i=1 s=1
i=1 s=2
i=1 s=3
i=1 s=4
i=1 s=5
i=1 s=6
i=1 s=7
i=1 s=8
i=1 s=9
i=1 s=10
i=1 s=11
i=1 s=12
...
```
From this output, we should be able to figure out two facts: (1) the variable
`i` is not changing; and (2) the variable `s` is infinitely growing by one. These
two facts will help us drawing the conclusion that the assignment `i = i + 1`
should be part of the loop statement.

Watching variables can help also debugging our programs when they do end but
do not provide the expected result. They should help us to identify the place
in the program where they are taking the wrong value.
