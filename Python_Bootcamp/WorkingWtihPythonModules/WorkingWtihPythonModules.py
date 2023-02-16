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
## Importing the module
import sys

## Returns the version of the Python interpreter
sys.version

## Other info about the interpreter
sys.implementation

## Returns the platform (linux, win32 or mac)
sys.platform

## Returns the PATH (directories where it searches for modules)
sys.path

my_list = list(range(100))
sys.getsizeof(my_list)  # returns the size of the list in memory

## Redirecting output to a file instead of stdout (console)
original_stdout = sys.stdout  # saving the original stdout

## Using a file as stdout, redirecting output to a file
with open('stdout.txt', 'w') as sys.stdout:
    print('Printing a string')
    x = 10
    print(f'x is {x}')

sys.stdout = original_stdout

import os

## IMPORTANT!
## You should always use a valid path according to your operating system


## Returns the file that defines the module
os.__file__  # => '/usr/lib/python3.7/os.py'

cwd = os.getcwd()  # => returns the current working directory
print(cwd)

## changes the current working directory, OS specific
os.chdir('/home/user1/python')  # Linux specific
os.chdir('C:\\Users')  # Windows specific

os.path.isfile('/etc/passwd')  # returns True if argument is a file
os.path.isdir('/tmp')  # returns True if argument is a directory

## Splits the extension from a pathname, returns a tuple
name, extention = os.path.splitext('/var/log/kern.log')  # name is 'kern', extention is '.log'

## Listing a directory
os.listdir('.')  # returns the entries in the current working directory as a list
os.listdir('C:\\Users')  # returns the entries in the directory as a list

os.path.getmtime('/etc/passwd')  # => 1547047769.9049096, returns file's last modification time as a timestamp
os.path.getsize('/etc/passwd')  # => 2691, returns the size of a file

os.mkdir('PATH/dir')  # creates a new directory in PATH, os specific

## Creates a new directory called dir1 in Windows (permissions required)
os.mkdir('C:\\dir1')

## Creates a new directory called dir1 in Linux
os.mkdir('~/dir1')