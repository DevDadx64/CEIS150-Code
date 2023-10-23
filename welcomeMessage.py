# -*- coding: utf-8 -*- 
# Print welcome message
print("Welcome to the message generator program! Please follow the instructions below.")

# Initialize User class
class User:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def __str__(self):
        return f"Welcome {self.name}! You are {self.age} years old and your favorite color is {self.color}."
    
# Define function to validate user input
def is_valid_string(s):
    for char in s:
        if not (char.isalpha() or char in [' ', '-']):
            return False
    return True if s else False

# Get user input
while True:
    name = input("Enter your name: ")
    if is_valid_string(name):
        break
    else:
        print("Invalid input! Please enter a valid name.")

while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError:
        print("Invalid input! Please enter a valid integer for age.")

while True:
    color = input("Enter your favorite color: ")
    if is_valid_string(color):
        break
    else:
        print("Invalid input! Please enter a valid color.")


# Create user object and print welcome message
user = User(name, age, color)
print(user)
