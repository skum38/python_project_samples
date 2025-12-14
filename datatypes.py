# LIST - Ordered, mutable collection of items
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
test=[ 123,2,"abc",4.56,False]

fruits.append("orange")
fruits.remove("banana")
test.insert (2,"sushi")
print(fruits)  # ['apple', 'cherry', 'orange']
print(test)  # [123, 2, 'sushi', 'abc', 4.56, False]


# SET - Unordered, unique collection of items
colors = {"red", "green", "blue"}
numbers_set = {1, 2, 3, 4, 5}

colors.add("yellow")
colors.remove("red")
colors.add("blue")  # duplicate, will not be added
colors.add("orange") 
print(colors)  # {'green', 'blue', 'yellow', 'orange'}


# TUPLE - Ordered, immutable collection of items
coordinates = (10, 20)
long=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
rgb = (255, 128, 0)
single = (42,)  # comma required for single element

print(coordinates[0])  # 10
# tuples cannot be modified after creation
print(long)  # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
long.index(5)   
long.__add__((11,12,13))


# DICTIONARY - Unordered, mutable collection of key-value pairs
person = {"name": "John", "age": 30, "city": "New York"}
user = {1: "admin", 2: "user", 3: "guest"}

person["email"] = "john@example.com"
print(person["name"])  # John
del person["city"]
print(person)  # {'name': 'John', 'age': 30, 'email': 'john@example.com'}
type(user)
print(type(user))  # <class 'dict'>

