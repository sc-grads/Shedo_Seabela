## Importing a module
import math

## Importing two or more modules
import sys, os

## Importing a module as an alias
import random as r

## Importing just the Response class from requests module
from requests import Response

## Importing a class from a module as an alias
from requests import Response as res

## Import everyting directly from shutil module into the global namespace
## TO BE AVOIDED!
from shutil import *

## The block of code below if will be executed only when the script is run directly (not imported in another script)
if __name__ == '__main__':
    print('Running the script directly. Not importing it as a module.')

    # Importing the os module
import os

    # Importing math as an alias
import math as my_math

    # Importing everything from random module directly
from random import *