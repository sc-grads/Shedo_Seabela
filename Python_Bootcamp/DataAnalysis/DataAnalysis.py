import pandas as pd
numbers = list(range(2, 11, 2))
s1 = pd.Series(numbers)
print(s1)
labels = list('abcde')
print(labels)

s2 = pd.Series(data=numbers, index=labels)
print(s2)
my_dict = dict(zip(['a', 'b', 'c'], [1, 2, 3]))
my_dict = dict(zip(['a', 'b', 'c'], [1, 2, 3]))
print(my_dict)

s3 = pd.Series(my_dict)
print(s3)


print(s3['a'])