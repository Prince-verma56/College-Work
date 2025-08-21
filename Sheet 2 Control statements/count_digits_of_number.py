# 8. Count digits of a number
N = int(input("Enter a number: "))
count = 0
while N > 0:
    count += 1
    N //= 10
print("Number of digits =", count)