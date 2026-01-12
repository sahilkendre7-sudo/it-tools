# if_else_examples.py
# Simple examples of if, elif, and else in Python

# Example 1: Check whether a number is positive, negative, or zero
num = int(input("Enter a number: "))

if num > 0:
    print("The number is positive")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero")


# Example 2: Check whether a number is even or odd
num2 = int(input("\nEnter another number: "))

if num2 % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")


# Example 3: Check eligibility to vote
age = int(input("\nEnter your age: "))

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")


# Example 4: Find the largest of two numbers
a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("First number is greater")
elif b > a:
    print("Second number is greater")
else:
    print("Both numbers are equal")


# Example 5: Grading system
marks = int(input("\nEnter marks: "))

if marks >= 75:
    print("Grade: Distinction")
elif marks >= 60:
    print("Grade: First Class")
elif marks >= 50:
    print("Grade: Second Class")
elif marks >= 35:
    print("Grade: Pass")
else:
    print("Grade: Fail")
