# Working with text files
content = open('../configuration.txt')
print(content.read())

print(content.closed)

# YOUR CODE STARTS HERE

ip_list = open('ip.txt')
ip_list = ip_list.read().splitlines()



