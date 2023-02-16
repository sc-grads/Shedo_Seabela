# Working with text files
import time

content = open('../configuration.txt')
print(content.read())

print(content.closed, '\n')

# YOUR CODE STARTS HERE

# ip_list = open('ip.txt')
# ip_list = ip_list.read().splitlines()

# writing on a file
n_file = open('new_text.txt', 'w')
n_file.write('this is a  new file')
n_file.write('\nThis is a second line')


n_file = open('new_text.txt', 'a')
n_file.write('\nthis is a third line with append mode')
n_file.write('\nThis is a second line')


n_file = open('new_text.txt', 'w')
n_file.write('\nthis is a  new file\n')
n_file.write('\nThis is a second line')

# project
fileS = open('devices.txt')
data = fileS.read().splitlines()
print(data)
devices = list()
for i in data:
    devices.append(i.split(':'))



# challenges
with open('macs.txt') as files:
    details = files.read().split()
    details = list(set())

with open('mac_unique.txt', 'w', newline='') as f:
    for mac in details:
        f.write(f'{mac}\n')

my_str = ''
my_str = open('sample_file.txt').read().splitlines()
my_str = '\n'.join(my_str)
print(my_str)
last = my_str[len(my_str)-5:]
my_str1 = '\n'.join(last)
print('THis is the last 5   \n', my_str1)
tmp_list = [line for line in my_str if line.strip() != '']

# write to a new file
with open('file_without_blanks.txt', 'w') as f:
    f.write(''.join(tmp_list))
def tail(file, n):
    my_str = open(file, 'r').read().splitlines()
    my_str = '\n'.join(my_str)
    last = my_str[len(my_str)-n]
    my_str1 = '\n'.join(last)
    return my_str1

# while True:
#     t = tail('devices.txt', 7)
#     print(t)
#     #time.sleep(3)
#     print('')
def counts(file):
    my_str = open(file, 'r').read().splitlines()
    li = len(my_str)
    words = 0
    for line in my_str:
        words += len(line.split())
    chars = 0
    for line in my_str:
        chars += len(list(line))

    return li, words, chars

print(counts('sample_file.txt'))