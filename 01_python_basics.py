"""
Python Basics Tutorial
======================

This file covers fundamental Python concepts you need to know before diving into pandas.
Run each section separately to understand the concepts.
"""

print("Welcome to Python Basics! 🐍")
print("=" * 40)

# ============================================================================
# 1. VARIABLES AND DATA TYPES
# ============================================================================

print("\n1. Variables and Data Types")
print("-" * 30)

# Numbers
age = 25
height = 5.9
print(f"Age: {age} (type: {type(age)})")
print(f"Height: {height} (type: {type(height)})")

# Strings
name = "Alice"
message = 'Hello, World!'
print(f"Name: {name} (type: {type(name)})")
print(f"Message: {message}")

# Booleans
is_student = True
is_graduated = False
print(f"Is student: {is_student} (type: {type(is_student)})")

# ============================================================================
# 2. LISTS - ORDERED COLLECTIONS
# ============================================================================

print("\n2. Lists - Ordered Collections")
print("-" * 30)

# Creating lists
fruits = ["apple", "banana", "orange", "grape"]
numbers = [1, 2, 3, 4, 5]
mixed = ["Alice", 25, True, 5.9]

print(f"Fruits: {fruits}")
print(f"Numbers: {numbers}")
print(f"Mixed data: {mixed}")

# Accessing elements (indexing starts at 0)
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")

# Adding elements
fruits.append("kiwi")
print(f"After adding kiwi: {fruits}")

# List operations
print(f"Number of fruits: {len(fruits)}")
print(f"Is 'apple' in fruits? {'apple' in fruits}")

# ============================================================================
# 3. DICTIONARIES - KEY-VALUE PAIRS
# ============================================================================

print("\n3. Dictionaries - Key-Value Pairs")
print("-" * 30)

# Creating dictionaries
person = {
    "name": "Bob",
    "age": 30,
    "city": "New York",
    "is_employed": True
}

print(f"Person: {person}")
print(f"Person's name: {person['name']}")
print(f"Person's age: {person['age']}")

# Adding new key-value pairs
person["email"] = "bob@email.com"
print(f"After adding email: {person}")

# Dictionary methods
print(f"Keys: {list(person.keys())}")
print(f"Values: {list(person.values())}")

# ============================================================================
# 4. CONTROL STRUCTURES
# ============================================================================

print("\n4. Control Structures")
print("-" * 30)

# If-elif-else statements
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")

# For loops
print("\nCounting 1 to 5:")
for i in range(1, 6):
    print(f"Count: {i}")

print("\nIterating through fruits:")
for fruit in fruits:
    print(f"Fruit: {fruit}")

# While loops
print("\nCountdown:")
countdown = 5
while countdown > 0:
    print(f"{countdown}...")
    countdown -= 1
print("Blast off! 🚀")

# ============================================================================
# 5. FUNCTIONS
# ============================================================================

print("\n5. Functions")
print("-" * 30)

def greet(name, age=None):
    """
    Function to greet a person
    
    Args:
        name (str): Person's name
        age (int, optional): Person's age
    
    Returns:
        str: Greeting message
    """
    if age:
        return f"Hello, {name}! You are {age} years old."
    else:
        return f"Hello, {name}!"

# Function calls
message1 = greet("Alice")
message2 = greet("Bob", 30)
print(message1)
print(message2)

def calculate_area(length, width):
    """Calculate the area of a rectangle"""
    area = length * width
    return area

rectangle_area = calculate_area(10, 5)
print(f"Rectangle area: {rectangle_area}")

# ============================================================================
# 6. LIST COMPREHENSIONS (ADVANCED)
# ============================================================================

print("\n6. List Comprehensions")
print("-" * 30)

# Traditional way
squares_traditional = []
for i in range(1, 6):
    squares_traditional.append(i ** 2)

# List comprehension way
squares_comprehension = [i ** 2 for i in range(1, 6)]

print(f"Squares (traditional): {squares_traditional}")
print(f"Squares (comprehension): {squares_comprehension}")

# Filtering with list comprehension
even_squares = [i ** 2 for i in range(1, 11) if i % 2 == 0]
print(f"Even squares: {even_squares}")

# ============================================================================
# 7. ERROR HANDLING
# ============================================================================

print("\n7. Error Handling")
print("-" * 30)

# Try-except blocks
def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"
    except TypeError:
        return "Error: Please provide numbers only!"

print(f"10 / 2 = {safe_divide(10, 2)}")
print(f"10 / 0 = {safe_divide(10, 0)}")
print(f"10 / 'a' = {safe_divide(10, 'a')}")

# ============================================================================
# EXERCISES
# ============================================================================

print("\n" + "=" * 50)
print("EXERCISES - Try these on your own!")
print("=" * 50)

print("""
1. Create a list of your favorite movies and print each one with its position number.

2. Create a dictionary representing a book with keys: title, author, year, pages.
   Then print a formatted string with all the information.

3. Write a function that takes a list of numbers and returns:
   - The sum of all numbers
   - The average of all numbers
   - The largest number

4. Create a list of numbers from 1 to 20, then use list comprehension to:
   - Get all even numbers
   - Get squares of odd numbers
   - Get numbers divisible by 3

5. Write a function that safely converts a string to an integer,
   returning 0 if conversion fails.
""")

# Example solutions (uncomment to see):
"""
# Exercise 1 solution:
movies = ["The Matrix", "Inception", "Interstellar"]
for i, movie in enumerate(movies, 1):
    print(f"{i}. {movie}")

# Exercise 3 solution:
def analyze_numbers(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    return {
        'sum': total,
        'average': average,
        'max': maximum
    }

result = analyze_numbers([1, 2, 3, 4, 5])
print(result)
"""

print("\nGreat job completing Python Basics! 🎉")
print("Next: Move on to 02_functions_and_modules.py")