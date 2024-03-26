# Chapter Three
import math

ratio = 10 / 2
ratio1 = 10 * math.log(ratio)
print(ratio1)
radians = 0.7
height = math.sin(radians)
print(height)


def cat_twice(part1, part2):
    cat = part1 + part2
    print(cat)


line1 = 'Bing tiddle '
line2 = ' tiddle bang.'
cat_twice(line1, line2)


# Exercise 3.2. A function object is a value you can assign to a variable or pass as an argument. For
# example, do_twice is a function that takes a function object as an argument and calls it twice:
# def do_twice(f):
#    f()
# f()
# Here’s an example that uses do_twice to call a function named print_spam twice.
# def print_spam():
#    print('spam')
# do_twice(print_spam)
# 1. Type this example into a script and test it.
# 2. Modify do_twice so that it takes two arguments, a function object and a value,
# and calls the function twice, passing the value as an argument.
# 3. Copy the definition of print_twice from earlier in this chapter to your script.
# 4. Use the modified version of do_twice to call print_twice twice, passing 'spam' as an
# argument.
# 5. Define a new function called do_four that takes a function object and a value and
# calls the function four times, passing the value as a parameter.
# There should be only two statements in the body of this function, not four.

def do_twice(f, val):
    f(val)
    f(val)


def print_twice(val):
    print(val)


do_twice(print_twice, 'spam')


def do_four(f, val):
    do_twice(f, val)
    do_twice(f, val)


do_four(print_twice, 'spam')


# Exercise 3.3. Note: This exercise should be done using only
# the statements and other features we have learned so far.
# 1. Write a function that draws a grid like the following:
# +----+----+ ||| ||| ||| ||| +----+----+ ||| ||| ||| ||| +----+----+
# Hint: to print more than one value on a line, you can print a comma-separated sequence of values:
# print('+', '-')
# By default, print advances to the next line, but you can override that behavior and put a
# space at the end, like this:
#     print('+', end=' ')
#     print('-')
# The output of these statements is '+ -' on the same line.
# The output from the next print statement would begin on the next line.

def print_pattern_one():
    print('+', 4 * '-', '+', 4 * '-', '+', end=' ')
    print()


def print_pattern_two():
    print('|', 4 * ' ', '|', 4 * ' ', '|', end=' ')
    print()
    print('|', 4 * ' ', '|', 4 * ' ', '|', end=' ')
    print()
    print('|', 4 * ' ', '|', 4 * ' ', '|', end=' ')
    print()
    print('|', 4 * ' ', '|', 4 * ' ', '|', end=' ')
    print()


def final_pattern(f1, f2):
    f1()
    f2()
    f1()
    f2()
    f1()


final_pattern(print_pattern_one, print_pattern_two)


# Write a function that draws a similar grid with four rows and four columns.


def four_print_pattern_one():
    print('+', 4 * '-', '+', 4 * '-', '+', '+', 4 * '-', '+', 4 * '-', '+',end=' ')
    print()


def four_print_pattern_two():
    print('|', 4 * ' ', '|', 4 * ' ', '|', '|', 4 * ' ', '|', 4 * ' ', '|', end=' ')
    print()
    print('|', 4 * ' ', '|', 4 * ' ', '|', '|', 4 * ' ', '|', 4 * ' ', '|', end=' ')
    print()
    print('|', 4 * ' ', '|', 4 * ' ', '|', '|', 4 * ' ', '|', 4 * ' ', '|', end=' ')
    print()
    print('|', 4 * ' ', '|', 4 * ' ', '|', '|', 4 * ' ', '|', 4 * ' ', '|', end=' ')
    print()


def four_final_pattern(f1, f2):
    f1()
    f2()
    f1()
    f2()
    f1()


four_final_pattern(four_print_pattern_one,four_print_pattern_two)