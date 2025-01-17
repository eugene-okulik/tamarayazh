my_dict = {
    "tuple": (1, 2, 3, 4, 5),
    "list": ["one", "two", "three", "four", "five"],
    "dict": {"name": "Kate", "surname": "Watson", "age": 35, "job:": "doctor", "city": "Texas"},
    "set": {100, "red", "text", 50, "green"}
}

print(my_dict["tuple"][-1])
my_dict["list"].append('six')
my_dict["list"].pop(1)
my_dict["dict"][('i am a tuple',)] = "new"
my_dict["dict"].pop("age")
my_dict["set"].add(3000)
my_dict["set"].discard("text")
print(my_dict)
