total = 0
# 9. Sum of digits of a number
N = int(input("Enter a number: "))
total = 0
while N > 0:
    digit = N % 10
    total += digit
    N //= 10
print("Sum of digits =", total)