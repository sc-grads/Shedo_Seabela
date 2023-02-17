import csv
with open('airtravel.csv', 'r') as content:
    reader = csv.reader(content)
    next(reader)
    for row in reader:
        print(row[3])
