"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

def calculate():


    """ A prefix-notation calculator"""

    print "Please enter the math operation and corresponding values: "
    # repeat forever:
    while True:
        # get input
        user_input = raw_input("> ")
        # tokenize input
        tokens = user_input.split(" ")
        action = tokens[0]
        inputs = tokens[1:]
        for i in range(len(inputs)):
            if inputs[i].isdigit():
                inputs[i] = float(inputs[i])
            else: 
                print "Please enter a valid math expression."


        # if the first token is "q":
        if action == 'q':
            # quit
            return
        # else:
        else:
            # decide which math function to call based on first token
            # define num1 and convert to float
            # **num1 = float(tokens[1])**

            # if only 1 number:
            if action in ['square', 'cube']:
                #if square then square()
                if action == 'square':
                    print square(inputs)
                #if cube then cube()
                if action == 'cube':
                    print cube(inputs)
            # if 2 or 3 numbers:
            elif action in ['+', '-', '*', '/',
                            'pow', 'mod', 'x+', 'cubes+']:
                # **num2 = float(tokens[2])**
                 # if + then add()
                if action == '+':
                    print add(inputs)
                 # if - then subtract()
                if action == '-':
                    print subtract(inputs)
                # if * then multiply()
                if action == '*':
                    print multiply(inputs)
               #  if / then divide()
                if action == '/':
                    print divide(inputs)
               #  if pow then pow()
                if action == 'pow':
                    print power(inputs)
                # if mod then mod()
                if action == 'mod':
                    print mod(inputs)
                # if x+ then add_mult()
                if action == 'x+':
                    print add_mult(inputs)
                # if cubes+ then add_cubes()
                if action == 'cubes+':
                    print add_cubes(inputs)
            else:
                print "Please enter a valid math operator."


calculate()
