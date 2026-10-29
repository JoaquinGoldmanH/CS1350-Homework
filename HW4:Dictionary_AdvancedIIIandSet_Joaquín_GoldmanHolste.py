# ============================================================
# LECTURE 3 - DICTIONARIES
# ============================================================

# ------------------------------------------------------------
# Unit 3.1 - Iterating Over Dictionaries
# ------------------------------------------------------------

inventory = {"apples": 50, "bananas": 30, "oranges": 20}
prices = {"laptop": 999, "phone": 699, "tablet": 449, "mouse": 25}
temps = {"Mon": 72, "Tue": 68, "Wed": 75, "Thu": 80, "Fri": 65}

# --- Beginner ---

for product in inventory:
    print(product)

total = sum(inventory.values())
print(total)

for product, quantity in inventory.items():
    print(f"{product}: {quantity}")

# --- Intermediate ---


for product in sorted(prices):
    print(product)


for product in sorted(prices, key=prices.get):
    print(product, prices[product])


most_expensive = max(prices.items(), key=lambda item: item[1])
print("Product:", most_expensive[0])
print("Price:", most_expensive[1])

# --- Advanced ---


average = sum(temps.values()) / len(temps)
print(average)


average = sum(temps.values()) / len(temps)
print(average)

hottest_day = None
coldest_day = None
for day, temp in temps.items():
    if hottest_day is None or temp > temps[hottest_day]:
        hottest_day = day
    if coldest_day is None or temp < temps[coldest_day]:
        coldest_day = day

print("Hottest:", hottest_day, temps[hottest_day])
print("Coldest:", coldest_day, temps[coldest_day])

average = sum(temps.values()) / len(temps)
count = 0
for temp in temps.values():
    if temp > average:
        count += 1
print(count)


# ------------------------------------------------------------
# Unit 3.2 - Nested Dictionaries
# ------------------------------------------------------------

products = {
    "laptop": {"price": 999, "stock": 15},
    "phone": {"price": 699, "stock": 40},
    "headphones": {"price": 199, "stock": 25},
}
company = {
    "Sales": {"Alice": 60000, "Bob": 55000},
    "Engineering": {"Carol": 95000, "Dave": 88000},
    "HR": {"Eve": 52000},
}

# --- Beginner ---

print(products["laptop"]["price"])

for product, info in products.items():
    print(product, info["stock"])

# --- Intermediate ---

countries = ["USA", "Canada", "Mexico"]
capitals = ["Washington", "Ottawa", "Mexico City"]
country_capital = dict(zip(countries, capitals))
print(country_capital)

products["tablet"] = {"price": 449, "stock": 30}
print(products)

for product, info in list(products.items()):
    if info["stock"] < 20:
        del products[product]
print(products)

# --- Advanced ---

for department, employees in company.items():
    print(department)
    for employee, salary in employees.items():
        print(employee, salary)

for department, employees in company.items():
    average = sum(employees.values()) / len(employees)
    print(department, average)

highest_name = ""
highest_salary = 0
for department, employees in company.items():
    for employee, salary in employees.items():
        if salary > highest_salary:
            highest_salary = salary
            highest_name = employee
print(highest_name, highest_salary)


# ------------------------------------------------------------
# Unit 3.3 - Dictionary Comprehensions
# ------------------------------------------------------------

scores = {"Alice": 92, "Bob": 65, "Carol": 78, "Dave": 85}
sales = [
    ("North", "Alice", 500),
    ("South", "Bob", 300),
    ("North", "Carol", 200),
    ("South", "Alice", 400),
    ("North", "Alice", 150),
]

# --- Beginner ---

cubes = {x: x**3 for x in range(1, 6)}
print(cubes)

temps = {"Mon": 72, "Tue": 68, "Wed": 75}
celsius = {
    day: (temp - 32) * 5 / 9
    for day, temp in temps.items()
}
print(celsius)

# --- Intermediate ---

passing = {
    name: score
    for name, score in scores.items()
    if score >= 70
}
print(passing)


def to_letter(score):
    """Convert a numeric score to a letter grade."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"


letter_grades = {
    name: to_letter(score)
    for name, score in scores.items()
}
print(letter_grades)

student_ids = {
    "Alice": 101,
    "Bob": 102,
}
id_lookup = {
    id_num: name
    for name, id_num in student_ids.items()
}
print(id_lookup)

# --- Advanced ---

region_totals = {}
for region, person, amount in sales:
    region_totals[region] = region_totals.get(region, 0) + amount
print(region_totals)

salesperson_totals = {}
for region, person, amount in sales:
    salesperson_totals[person] = (
        salesperson_totals.get(person, 0) + amount
    )
print(salesperson_totals)

nested = {}
for region, person, amount in sales:
    if region not in nested:
        nested[region] = {}
    nested[region][person] = (
        nested[region].get(person, 0) + amount
    )
print(nested)


# ============================================================
# LECTURE 4 - SETS
# ============================================================

# ------------------------------------------------------------
# Unit 1 - Creating Sets
# ------------------------------------------------------------

# --- Beginner ---

vowels = {"a", "e", "i", "o", "u"}
print(vowels)

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_numbers = set(numbers)
print(unique_numbers)
print(len(unique_numbers))

empty = set()
print(type(empty))

# --- Intermediate ---

text = "mississippi"
unique_chars = set(text)
print(unique_chars)
print(len(unique_chars))

emails = [
    "a@b.com",
    "c@d.com",
    "a@b.com",
    "e@f.com",
    "c@d.com",
]
unique_emails = list(set(emails))
print(unique_emails)

s = {(1, 2), (3, 4)}
print(s)

# --- Advanced ---

import time

big_set = set(range(1000000))
big_list = list(range(1000000))

start = time.time()
999999 in big_set
print("Set:", time.time() - start)

start = time.time()
999999 in big_list
print("List:", time.time() - start)

my_dict = {
    frozenset({"a", "b"}): "value"
}
print(my_dict)

edges = [(1, 2), (2, 3), (1, 3), (3, 4)]
nodes = set()
for a, b in edges:
    nodes.add(a)
    nodes.add(b)
print(nodes)


# ------------------------------------------------------------
# Unit 2 - Set Operations
# ------------------------------------------------------------

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
morning_shift = {"Alice", "Bob", "Carol", "Dave"}
evening_shift = {"Bob", "Carol", "Eve"}
weekend_shift = {"Carol", "Frank", "Alice"}
prereqs_met = {"Ana", "Ben", "Cara", "Dan"}
has_space = {"Ana", "Ben", "Cara", "Eli"}
paid_tuition = {"Ana", "Cara", "Dan", "Eli"}

# --- Beginner ---

print(a | b)   # union: items in a OR b
print(a & b)   # intersection: items in a AND b
print(a - b)   # difference: items in a but NOT in b

# --- Intermediate ---

all_shifts = morning_shift & evening_shift & weekend_shift
print(all_shifts)

any_shift = morning_shift | evening_shift | weekend_shift
print(any_shift)

morning_only = morning_shift - evening_shift - weekend_shift
print(morning_only)

employees = morning_shift | evening_shift | weekend_shift
exactly_one = set()
for employee in employees:
    count = (
        (employee in morning_shift) +
        (employee in evening_shift) +
        (employee in weekend_shift)
    )
    if count == 1:
        exactly_one.add(employee)
print(exactly_one)

# --- Advanced ---

eligible = prereqs_met & has_space & paid_tuition
print(eligible)

not_paid = prereqs_met - paid_tuition
print(not_paid)

all_students = prereqs_met | has_space | paid_tuition
eligible = prereqs_met & has_space & paid_tuition
need_help = all_students - eligible
print(need_help)


# ------------------------------------------------------------
# Unit 3 - Set Methods and Comprehensions
# ------------------------------------------------------------

alice = {"python", "java", "sql", "c"}
bob = {"python", "javascript", "sql"}
carol = {"python", "sql", "rust"}

# --- Beginner ---

s = {1, 2, 3}
s.add(4)
s.remove(1)
print(s)

evens = {x for x in range(21) if x % 2 == 0}
print(evens)

colors = {"red", "blue"}
colors.discard("green")
print(colors)

# --- Intermediate ---

data = [4, 5, 2, 4, 8, 5, 2, 1, 9, 4]
seen = set()
result = []
for item in data:
    if item not in seen:
        seen.add(item)
        result.append(item)
print(result)

sentence = "To be or not to be that is the question"
words = {
    word.lower()
    for word in sentence.split()
}
print(words)

expected = set(range(1, 11))
actual = {1, 2, 4, 5, 7, 8, 10}
missing = expected - actual
print(missing)

# --- Advanced ---


def find_duplicates(lst):
    """Return a set of items that appear more than once in lst."""
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return duplicates


print(find_duplicates([1, 2, 2, 3, 3, 3, 4]))

print(alice & bob & carol)   # skills all three share
print(alice - bob - carol)   # skills only Alice has
print(alice | bob | carol)   # every skill anyone has


def common_chars(str1, str2):
    """Return the characters that appear in both strings."""
    return set(str1) & set(str2)


print(common_chars("hello", "world"))
