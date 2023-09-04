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
# this inserts the folder in which the script exists in into the path string, so that when we look for packages we will also be able to import our scripts.
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))

# this match the folder/project name and will import as the __init__ of this project
from Thors_python_style_guide import example_function


### Clases
# a setup I like is to set up assignments as static classes, so that I can keep the entirety of an assignment in one file but still easily turn of segment while running.

class part_one:
    # each method/function should be like a main function for the assignment
    def one_a(self, report=True):
        #  declaration of assignment variables
        a = 5
        b = 2

        # math and function calls

        result = a + b

        # report results
        if report: print(f'variable a ({a}) plus variable b ({b} gives {result}')

        # you can return the variables as a dict if you need them in another part.
        return dict(a=a, b=b, result=result)

    def one_b(self):

        c = 6

        # getting variables from part a
        part_one_dict = self.one_a(report=False)

        result = (part_one_dict['a'] + part_one_dict['b']) / c

        print(f'a plus b divided by c ({c}) is {result}')


class part_two:
    def two_a(self): ...
    def two_b(self): ...


### Fucntions



def main():
    assignment_1 = part_one() # create a callable object for the assignment
    assignment_1.one_a()
    assignment_1.one_b()
    # this runs part one a and b of assignment one, and you can turn of running parts of the code by out commenting.


if __name__ == '__main__':
    main()
