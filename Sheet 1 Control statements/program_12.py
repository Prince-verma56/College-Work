# Problem 12: You are given 3 integer angles A, B, and C of a triangle. Check if the triangle is valid.
a = int(input("Enter first angle: "))
b = int(input("Enter second angle: "))
c = int(input("Enter third angle: "))
if a+b+c == 180:
    print("Valid Triangle")
else:
    print("Invalid Triangle")