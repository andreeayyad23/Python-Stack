# test.py

# Print initial messages
print("Hello World!")
print("Hello Python")
print(42)

# Variable declarations and type checking
name = "Andree"
print(type(name))  # Output: <class 'str'>

# String concatenation and formatting
first_name = "Hello"
last_name = "World!"
full_name = f"{first_name} {last_name}"
print(full_name)  # Output: Hello World!

# Age calculation and conversion
age = 23
age += 1  # Corrected from age =+ 1
print(f"Your age is: {age}")  # Output: Your age is: 24

# Weight declaration and formatting
weight = 95.5
print(weight)  # Output: 95.5
print(f"Hello {weight} cm")  # Output: Hello 95.5 cm

# Boolean variable and type checking
is_human = True
print(type(is_human))  # Output: <class 'bool'>

# String operations
name = "Zen"
print("My name is", name)  # Output: My name is Zen

name = "Andree"
print(name.replace("A", "B"))  # Output: Bndree

print(name * 6)  # Output: AndreeAndreeAndreeAndreeAndreeAndree

# String formatting with placeholders
first_name = "Clara"
last_name = "Loro"
age = 24
print(f"My name is {first_name} {last_name} and I am {age} years old.")
# Output: My name is Clara Loro and I am 24 years old.

# Input handling and type conversion
total = 35
user_val = "26"
total = total + int(user_val)  # total becomes 61
print(total)  # Output: 61

# String length calculation
print(len('Coding Dojo'))  # Output: 11

# Fave food concatenation
fave_food1 = "sushi"
fave_food2 = "pizza"
print(f"I love to eat {fave_food1} and {fave_food2}")
# Output: I love to eat sushi and pizza

# Intro message with fave foods
intro = "I love eating in general especially"
fave_food3 = "falafel"
fave_food4 = "shawarma"
print(f"{intro} {fave_food3} {fave_food4}")
# Output: I love eating in general especially falafel shawarma