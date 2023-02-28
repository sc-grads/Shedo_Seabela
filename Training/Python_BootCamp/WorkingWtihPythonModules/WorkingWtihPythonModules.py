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
os.listdir('')  # returns the entries in the current working directory as a list
os.listdir('C:\\Users')  # returns the entries in the directory as a list

os.path.getmtime('/etc/passwd')  # => 1547047769.9049096, returns file's last modification time as a timestamp
os.path.getsize('/etc/passwd')  # => 2691, returns the size of a file

os.mkdir('PATH/dir')  # creates a new directory in PATH, os specific

## Creates a new directory called dir1 in Windows (permissions required)
os.mkdir('C:\\dir1')

## Creates a new directory called dir1 in Linux
os.mkdir('~/dir1')

## The shutil module
##############################

## Importing the module
import shutil

## Copying a.txt to b.txt. a.txt is in the current working directory
## It copies only file's content and not permissions or times
## If the destination file exists, it will be overwritten
shutil.copyfile('a.txt', 'b.txt')

# Copying a.txt to c.txt. a.txt is in the current working directory
# It copies the file data and the file’s permission mode. Other metadata is not preserved
shutil.copy('a.txt', 'c.txt')

## Use absolute PATHs specific to your OS
# shutil.copy('C:\\Users\\ad\\Desktop\\dir1\\file1.txt','C:\\Users\\ad\\Desktop\\dir2')


## copy2() function preserves all file's metadata
## It copies a.txt from the current directory to c.txt in dir1 directory which is in the current directory
shutil.copy2('a.txt', 'dir1/c.txt')

## Copying an entire directory. dir1 is a directory in the current working dirrectory
shutil.copytree('dir1', 'dir2')

## Moving or renaming files or directory
## It moves c.txt from the current directory to dir2/ which is another directory in the current directory
shutil.move('c.txt', 'dir2/')
shutil.move('dir2', 'dir1')  # moves a directory into another directory

## Renaming a file
## If the source and the destination are in the same directory, move() renames the file
shutil.move('b.txt', 'x.txt')  # renaming b.txt to x.txt

## Removing a directory. dir2 is a directory in the current working directory
shutil.rmtree('dir2')

## If trying to remove a file, it raises an exception
# shutil.rmtree('a.txt')     # => ERROR

## You should use os.remove() to remove a file
import os

os.remove('b.txt')

## Running system commands using os module
import os

## Running 'arp -a' command and getting the output
output = os.popen('arp -a').read()
print(output)  # => (192.168.0.1) at 90:5c:44:05:91:26 [ether] on wlo1

## Running 'ipconfig' command on Windows and getting the output
# output = os.popen('ipconfig').read()
# print(output)   # printing the output of ipconfig command

## It's not recommended to execute commands using os.system()
# os.system('whatever command')


## Running system commands using subprocess module
import subprocess

# subprocess.check_output() is used to run a command and capture the output
# subprocess.check_call() is used to run a command without capture the output

## The command and its options and arguments is a list
cmd = ['arp', '-a']
output = subprocess.check_output(cmd)  # running the command and getting the output
print(output.decode())  # output is of type bytes, decoding to string and print it out

cmd = ['ping', '-c 1', '8.8.8.8']  # Linux command
# cmd = ['ping', '-n 1', '8.8.8.8']     # Windows command
output = subprocess.check_output(cmd)  # Running the command and getting the output
print(output.decode())  # Decoding from bytes to string

# Output:
# --- 8.8.8.8 ping statistics ---
# 1 packets transmitted, 1 received, 0% packet loss, time 0ms
# rtt min/avg/max/mdev = 34.776/34.776/34.776/0.000 ms


## Spliting the command string to a list, executing it and decoding the output to a string
output = subprocess.check_output('ping -c 1 8.8.8.8'.split()).decode()
print(output)

## Importing the module
import decimal
from decimal import Decimal

## There is no exact representation for some float numebers. We can't use arithmetic operators with some floats
a = 0.3
# a displayed with 25 decimal points
print(format(a, '.25f'))  # => 0.2999999999999999888977698
print(a * 3 == 0.9)  # => False

## Creating a integer using the Decimal class
## The argument is an integer or a string
x = Decimal(5)
y = Decimal('5')
print(x == y)  # => True

## Creating a float using the Decimal class
## The argument should be the float as a string
x = Decimal(0.3)  # WRONG!
y = Decimal('0.3')  # CORRECT!
z = Decimal('0.9')

print(x == y)  # => False
print(y * 3 == z)  # => True

## There are methods in the Decimal class that should be used instead of methods from the maths module
x = Decimal(0.3)
sq = x.sqrt()
print(format(sq, '.20f'))  # => 0.54772255750516610332

import math

sq = math.sqrt(0.3)
print(format(sq, '.20f'))  # => 0.54772255750516607442

## Getting the context
print(decimal.getcontext())
# Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, capitals=1, clamp=0,
# flags=[FloatOperation], traps=[InvalidOperation, DivisionByZero, Overflow])

print(decimal.getcontext().prec)  # => 28
print(decimal.getcontext().rounding)  # => ROUND_HALF_EVEN

## Chainging the precision and the rounding
decimal.getcontext().prec = 4
decimal.getcontext().rounding = decimal.ROUND_HALF_DOWN