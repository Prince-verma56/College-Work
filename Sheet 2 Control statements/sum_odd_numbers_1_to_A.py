# 7. Sum of odd numbers from 1 to A
A = int(input("Enter a number: "))
total = 0
for i in range(1, A+1, 2):
    total += i
print("Sum of odd numbers =", total)