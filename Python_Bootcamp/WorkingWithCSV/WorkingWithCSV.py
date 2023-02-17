import csv
with open('airtravel.csv', 'r') as content:
    reader = csv.reader(content)
    next(reader)
    for row in reader:
        print(row[3])


with open('people.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    csvdata = (5, 'Anne', 'Amsterdam')
    writer.writerow(csvdata)


with open('numbers.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['x', 'x**2', 'x**3', 'x**4'])
    for x in range(1, 101):
        writer.writerow([x, x ** 2, x ** 3, x ** 4])