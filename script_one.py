# Imports
#
# start with the native python packages that you need, such as sys and pathlib.
import sys
import pathlib
import argparse
from typing import Tuple, Sequence

# then downloadable packages such as numpy
import numpy as np

# local Import
# this inserts the folders location into the path string, so that when we look for packages we will also be able to import our other scripts.
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))

# this match the folder/project name and will import as the __init__ of this project
from Thors_python_style_guide import example_function


# class declaration.


# Function declarations

# I like this order for my functions:
# functions for reading data, such as cvs files, txt files or databases
# math functions.
# major work function that apply the math functions.
# output functions such as functions the write files, plots or update databases
# trouble shoot function.

# read or load Functions
# A functions for reading data should take in the path for the data file and return information in your python objects of choice, there should not be to many functions or data manipulation beyound that in this function.

# Math Functions
# An example of a simple math functions
def vector_plus(v1: Sequence[float], v2: Sequence[float]) -> Sequence[float]: return [c1+c2 for c1, c2 in zip(v1, v2)]

# Work Functions
# The work functions are were most of the work happen, in the main() function I talk about how it should be easy to translate into a flow chart, in that picture the names/blocks in the flow chart should primarily be functions in this category.

# Output Functions
# These functions should take the return values/objects of your work functions and write them into csv, plots, database or some other system for keeping the data outside the script


# Trouble shoot function.
def silent_print(x):
    # print doesn't return a value so by making this i have a function i can set in anywhere in the code and not having the print get in the way.
    # such as within arguments of a function
    print(x)
    return x


# main declaration
def main(arg_1: str): # by adding : after an argument we can declare the type we expect the argument to be and that will be helpful for any one looking at the code. the package Typing handles this.

    # in here goes the main function of the script
    # it should primarily be function calls and a variable declarations
    # an ideal main function should be directly translatable to a flow graph over the scripts function with its main boxes explained by function names.
    # a good rule if you ever feel like you need to name a block of code in here with a comment then it should have been declared as a function

    # A main function should not have a return, since it should represent the entirety of the script running order.

    example_function()


if __name__ == '__main__':
    # this part of the code will only run if the script it the top level script,
    # that means that anything in here will not run if the script gets imported.
    # it can be seen as the start of the script.
    # and for me the function of this 'if' is to set up the script arguments with argparse and parse that into the main().
    # Often i use argparse to state what files go into the scripts and what form the output should have, such as tables or plots.

    # if you don't have arguments for the script, then there is no need for having arg parse, and you can just call main() from here

    parser = argparse.ArgumentParser()
    parser.add_argument('argument', type=str, help='an argument that can be filled from the command line')
    args = parser.parse_args()

    main(
        # any arguments from argparse to the main goes here,
        arg_1=args.argument # note that the attribute of the args is the first string in the add_argument method.
    )

