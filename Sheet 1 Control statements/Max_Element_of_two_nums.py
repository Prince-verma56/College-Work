# Problem 13: Write a program to input two numbers (A & B) and print the maximum element.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Maximum is:", a if a > b else b)