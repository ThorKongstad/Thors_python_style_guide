# Imports
#
# start with the native python packages that you need, such as sys and pathlib.
import sys
import pathlib
import argparse

# then downloadable packages such as numpy

# local Import
# this inserts the folder in which the script exists in into the path string, so that when we look for packages we will also be able to import our scripts.
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))

# this match the folder/project name and will import as the __init__ of this project
from Thors_python_style_guide import example_function


# class declaration.


# Function declarations

# i like this order for my functions:
# functions for reading data, such as cvs files, txt files or databases
# math functions.
# major work function that apply the math functions.
# output functions such as functions the write files, plots or update databases
# trouble shoot function.

# this is a trouble shoot function.

def silent_print(x):
    # print doesn't return a value so by making this i have a function i can set in anywhere in the code and not get in the way
    print(x)
    return x


# main declaration
def main(arg_1: str): # by adding : after an argument we can declare the type we expect the argument to be and that will be helpful for any one looking at the code. the package Typing handles this.

    # in here goes the main function of the script
    # it should primarily be function calls and a variable declarations
    # an ideal main function should be directly translatable to a flow graph over the scripts function with its main boxes explained by function names.
    # a good rule if you ever feel like you need to name a block of code in here with a comment then it should have been declared as a function

    # A main function should not have a return, since it should represent the entirety of the script running order.

    pass # pass is a do nothing and ignore that the function is empty, don't mind it.


if __name__ == '__main__':
    # this part of the code will only run if the script it the top level script,
    # that means that anything in here will not run if the script gets imported.
    # it can be seen as the start of the script.
    # and for me the main function is to set up the script arguments with argparse and parse that into the main().

    parser = argparse.ArgumentParser()
    parser.add_argument('argument', type=str, help='an argument that can be filled from the command line')
    args = parser.parse_args()

    main(
        # any arguments from argparse to the main goes here,
        arg_1=args.argument # note that the attribute of the args is the first string in the add_argument method.
    )

    pass
