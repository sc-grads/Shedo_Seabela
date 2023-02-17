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