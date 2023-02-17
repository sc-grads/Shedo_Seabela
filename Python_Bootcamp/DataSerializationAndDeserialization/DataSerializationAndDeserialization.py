import pickle, json
friends = {"Dan": (20, "London", 13242252), "Maria": [25, "Madrid", 34232424]}
with open('friends.dat', 'wb') as f:
    pickle.dump(friends, f)
with open('friends.dat', 'rb') as f:
    obj = pickle.load(f)

    print(type(obj))
    print(obj)

friends = {"Dan": (20, "London", 13242252), "Maria": [25, "Madrid", 34232424]}


with open('friends.json', 'wt') as f:
    json.dump(friends, f, indent=4)


json_string = json.dumps(friends, indent=4)
print(json_string)

with open('friends.json') as f:
    obj = json.load(f)

    print(type(obj))
    print(obj)


json_string = """{
    "Dan": [
        20,
        "London",
        13242252
    ],
    "Maria": [
        25,
        "Madrid",
        34232424
    ]
}"""

obj = json.loads(json_string)
print(type(obj))
print(obj)

# Challenges
# Serializing to file
def serialize(obj, file, type):
    if type == 'pickle':
        import pickle
        with open(file, 'wb') as f:
            pickle.dump(obj, f)
    elif type == 'json':
        import json
        with open(file, 'w') as f:
            json.dump(obj, f)
    else:
        print('Invalid serialization. Use pickle or json!')



def deserialize(file, type):
    if type == 'pickle':
        import pickle
        with open(file, 'rb') as f:
            obj = pickle.load(f)
        return obj
    elif type == 'json':
        import json
        with open(file, 'r') as f:
            obj = json.load(f)
            return obj
    else:
        print('Invalid serialization. Use pickle or json!')


if __name__ == "__main__":
    d1 = {'a': 'x', 'b': 'y', 'c': 'z', 30: (2, 3, 'a')}

    # Serializing using pickle
    serialize(d1, 'a.dat', 'pickle')

    # Deserializing
    myDict = deserialize('a.dat', 'pickle')
    print(f'pickle: {myDict}')

    print('#' * 20)

    # serializing using pickle
    serialize(d1, 'a.json', 'json')

    # deserializing
    x = deserialize('a.json', 'json')

    print(f'json: {x}')