import pickle
friends = {"Dan": (20, "London", 13242252), "Maria": [25, "Madrid", 34232424]}
with open('friends.dat', 'wb') as f:
    pickle.dump(friends, f)
with open('friends.dat', 'rb') as f:
    obj = pickle.load(f)

    print(type(obj))
    print(obj)