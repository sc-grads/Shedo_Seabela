# Working with text files
content = open('../configuration.txt')
print(content.read())

print(content.closed)

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

print(devices)