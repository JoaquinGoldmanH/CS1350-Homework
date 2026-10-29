Unit 1.1
Beginner:
my_info = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science"
}

Intermediate:
menu = {
    "burger": 8.99,
    "fries": 3.49,
    "pizza": 11.99,
    "salad": 6.75
}

course_credits = {
    "CS1350": 3,
    "MATH1400": 4,
    "ENG1010": 3,
    "BIO1100": 4
}

Advanced:
weekly_temps = dict([
    ("Monday", 72),
    ("Tuesday", 75),
    ("Wednesday", 68),
    ("Thursday", 70),
    ("Friday", 77),
    ("Saturday", 80),
    ("Sunday", 74)
])

Unit 1.2
Beginner:
pet = {"name": "Buddy", "type": "dog", "age": 3}

print(pet["name"])
print(pet["age"])

Intermediate:
pet = {"name": "Buddy", "type": "dog", "age": 3}

# 1. Safely access a missing key with get()
print(pet.get("color", "unknown"))

# 2. Check if a student passed a course using get()
grades = {"CS101": "A", "MATH150": "B", "ENG110": "C"}
course = "CS101"

if grades.get(course) is not None:
    print(f"Student passed {course} with grade {grades[course]}")
else:
    print(f"{course} not found")

Advanced:
products = {"laptop": 999.99, "mouse": 29.99, "keyboard": 79.99}

def find_price(products_dict, product_name):
    price = products_dict.get(product_name)
    if price is not None:
        return price
    return "Product not available"

# Test with an existing product
print(find_price(products, "laptop"))   # 999.99

# Test with a non-existing product
print(find_price(products, "monitor"))   # Product not available

Unit 1.3
Beginner:
inventory = {}

# Add items here
inventory["apples"] = 10
inventory["bananas"] = 20
inventory["oranges"] = 15

print(inventory)

Intermediate:
scores = {"Team A": 45, "Team B": 38}

# 1. Update Team B and add Team C
scores["Team B"] = 52
scores["Team C"] = 41

# 2. Remove Team A using pop() and print the removed score
removed_score = scores.pop("Team A")
print("Removed Team A score:", removed_score)

print(scores)

Advanced:
# 1. Start with an empty cart dictionary
cart = {}

# 2. Add 3 items with prices
cart["apple"] = 1.50
cart["bread"] = 2.25
cart["milk"] = 3.10

# 3. Update the price of one item
cart["bread"] = 2.75

# 4. Remove one item and print what was removed
removed_item = cart.pop("milk")
print("Removed item:", removed_item)

# 5. Print the final cart
print("Final cart:", cart)

# Bonus: Calculate the total price of remaining items
total = sum(cart.values())
print("Total price:", total)


Unit 2.1
Beginner:

a) "student_name"      # valid (reason: strings are immutable and hashable)
b) [1, 2, 3]          # invalid (reason: lists are mutable and unhashable)
c) 100                # valid (reason: integers are hashable)
d) ("x", "y")         # valid (reason: tuples are immutable and hashable)
e) {"a": 1}           # invalid (reason: dictionaries are mutable and unhashable)
f) frozenset({1,2})   # valid (reason: frozenset is immutable and hashable)

Intermediate:
1)
locations = {
    (40.7, -74.0): "New York",
    (34.0, -118.2): "Los Angeles"
}
print(locations)

2)
{'a': 3, 'b': 4}
2

3)
print(hash("Alice"))   
print(hash(100))       


Advanced:
1)
scores = {
    ("Alice", "Tetris"): 1200,
    ("Bob", "Snake"): 980,
    ("Charlie", "Pong"): 1450
}

print(scores[("Alice", "Tetris")]) 

2)
import time

n = 100_000
lst = list(range(n))
d = {x: x for x in range(n)}

target = n - 1

start = time.perf_counter()
_ = target in lst
list_time = time.perf_counter() - start

start = time.perf_counter()
_ = target in d
dict_time = time.perf_counter() - start

print(f"List check time: {list_time:.8f} seconds")
print(f"Dictionary check time: {dict_time:.8f} seconds")

if list_time > dict_time:
    print(f"Dictionary is faster by {list_time / dict_time:.2f}x")
else:
    print("Dictionary is not faster in this run")


Unit 2.2

Beginner:
temps = {"Monday": 72, "Tuesday": 75, "Wednesday": 68}

# 1. Print all the day names using keys()
print("Days:", list(temps.keys()))

# 2. Print all the temperatures using values()
print("Temperatures:", list(temps.values()))

# 3. Print how many days are in the dictionary
print("Number of days:", len(temps))

Intermediate:

temps = {"Monday": 72, "Tuesday": 75, "Wednesday": 68}

# 1. Find and print the highest and lowest temperatures
highest_day = max(temps, key=temps.get)
lowest_day = min(temps, key=temps.get)

print("Highest:", highest_day, temps[highest_day])
print("Lowest:", lowest_day, temps[lowest_day])

# 2. Check if "Friday" is in the dictionary
if "Friday" in temps:
    print("Friday is in the dictionary.")
else:
    print("Friday is not in the dictionary.")

# 3. Use setdefault() to add "Thursday" with a value of 70 only if it doesn't exist
temps.setdefault("Thursday", 70)
print("After setdefault:", temps)

# 4. Demonstrate that views are dynamic
keys_view = temps.keys()
print("Initial keys view:", list(keys_view))

temps["Friday"] = 71
print("Updated keys view:", list(keys_view))

Advanced:
import sys

prices = {"laptop": 999, "phone": 699, "tablet": 449, "watch": 299}

# 1. Calculate the total value and average price
total_value = sum(prices.values())
average_price = total_value / len(prices)

print("Total value:", total_value)
print("Average price:", average_price)

# 2. Find the most and least expensive items
most_expensive_item = max(prices.items(), key=lambda x: x[1])
least_expensive_item = min(prices.items(), key=lambda x: x[1])

print("Most expensive:", most_expensive_item)
print("Least expensive:", least_expensive_item)

# 3. Compare memory usage between keys() view and list(prices.keys())
keys_view = prices.keys()
keys_list = list(prices.keys())

print("keys() view size:", sys.getsizeof(keys_view))
print("list(keys()) size:", sys.getsizeof(keys_list))

# 4. Use update() to add 3 new products, then show all products
prices.update({
    "mouse": 59,
    "keyboard": 89,
    "monitor": 249
})

print("Updated products:", prices)

Unit 2.3

Beginner:
1)
colors = {"apple": "red", "banana": "yellow", "grape": "purple"}

# 1. Use items() to print each fruit and its color
for fruit, color in colors.items():
    print(f"The {fruit} is {color}")

The apple is red
The banana is yellow
The grape is purple

2)
[("apple", "red"), ("banana", "yellow"), ("grape", "purple")]

Intermediate:

prices = {"coffee": 4.50, "tea": 3.00, "juice": 5.25}

# 1. Print each item with 10% tax added
for item, price in prices.items():
    taxed = price * 1.10
    print(f"{item}: ${price:.2f} + tax = ${taxed:.2f}")

# 2. Count items costing more than $4.00
count = sum(1 for price in prices.values() if price > 4.00)
print("Items over $4.00:", count)

# 3. Swap x and y in one line using tuple unpacking
x, y = 10, 20
x, y = y, x
print("x =", x, "y =", y)

# 4. Extended unpacking
nums = [1, 2, 3, 4, 5]
first, *middle, last = nums
print("first =", first)
print("middle =", middle)
print("last =", last)

Advanced:
import time

scores = {"Alice": 88, "Bob": 65, "Carol": 92, "Dave": 71, "Eve": 58}

# 1. Highest score using max() and items()
highest_student, highest_score = max(scores.items(), key=lambda item: item[1])
print("Highest scorer:", highest_student, highest_score)

# 2. Split into passed and failed
passed = {}
failed = {}

for student, score in scores.items():
    if score >= 70:
        passed[student] = score
    else:
        failed[student] = score

print("Passed:", passed)
print("Failed:", failed)

# 3. Average and deviation from average
average = sum(scores.values()) / len(scores)
print("Class average:", average)

deviations = {student: score - average for student, score in scores.items()}
print("Deviations:", deviations)

# 4. Performance test: items() iteration vs keys() with lookup
d = {str(i): i for i in range(50_000)}

start = time.perf_counter()
for _, value in d.items():
    _ = value
items_time = time.perf_counter() - start

start = time.perf_counter()
for key in d.keys():
    _ = d[key]
keys_time = time.perf_counter() - start

print(f"items() iteration: {items_time:.6f} seconds")
print(f"keys() + lookup: {keys_time:.6f} seconds")

