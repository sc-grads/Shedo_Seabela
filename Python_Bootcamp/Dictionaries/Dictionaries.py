# Create a dictionary called user with 4 key: value pairs
user = {'name': 'Shedo', 'age': 25, 'location': "Kempton park", 'email': 'ShedoSeabela.com'}

song = {'artist': 'John Winston Ono Lennon', 'name': 'Imagine', 'year': 1971}
# Calculating sum
money = {
    'bank': 8564.61,
    'paypal': 1998.21,
    'cash': 480,
    'payoneer': 250.5
}

# YOUR CODE STARTS HERE
total_amount = 0.0
for x in money.values():
    total_amount = total_amount + x
print(total_amount)
# Use a for loop to iterate over the dictionary and calculate the total amount.
# Save it to a variable called total_amount and print its value!

visits = {'Monday': 5000,
           'Tuesday': 3000,
           'Wednesday': 4000,
           'Thursday': 4500,
           'Friday': 5000,
           'Saturday': 2000,
           'Sunday': 1500
            }

# ## YOUR CODE STARTS HERE
total_visits = 0
for i in visits.values():
    total_visits += i

percentage = {i: (x / total_visits) * 100 for i, x in visits.items()}
print(percentage)
