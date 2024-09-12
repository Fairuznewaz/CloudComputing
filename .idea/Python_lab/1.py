#Problem-1: print your own message

print("Name: Fairuz")
print("Age:25")
print("Hobby: Reading")

#Problem-2: personalized greeting
#The + operator is used to concatenate strings.

name = input("Fairuz")
print("Helllo," + name + "!")

#Problem-3: comment your code

# This is a single-line comment
print("This will run.")

"""
This is a multi-line comment
It can span multiple lines
"""
print("This will also run.")

# This program prints the first five multiples of 3
for i in range(1, 6):
    print(i * 3)  # Multiply the current number by 3

#Problem-4: basic arithmetic operations
#Python can be used to perform basic arithmetic operations, just like a calculator.

# Addition
print("37 + 5 =", 37 + 5)

# Subtraction
print("100 - 2 =", 100 - 2)

# Multiplication
print("45 * 7 =", 45 * 7)

# Division
print("15 / 3 =", 15 / 3)

# Exponentiation
print("50 ** 3 =", 50 ** 3)

#Problem-5 : store your birth year

age = 25
current_year = 2024
birth_year = current_year - age
print("Your birth yhear is:", birth_year)


#Problem-7 : data types identification
#int for integers (whole numbers).
#'float' for floating-point numbers (decimals).
#'str' for strings (text).
#'bool' for Boolean values (True or False).

x = 5        # Integer
y = 3.14     # Float
name = "John" # String
is_active = True  # Boolean

print("x is of type:", type(x))
print("y is of type:", type(y))
print("name is of type:", type(name))
print("is_active is of type:", type(is_active))

#Problem-8 : swap two variables

a = 10
b = 20

print("Before swapping: a =", a, "b =", b)

# Swapping the values
a, b = b, a

print("After swapping: a =", a, "b =", b)

#Problem-9 : Simple Interest Calculator

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time (in years): "))

simple_interest = (principal * rate * time) / 100
print("The simple interest is:", simple_interest)