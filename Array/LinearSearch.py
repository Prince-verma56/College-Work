arr = [2, 3, 4, 5, 6]
target = 5

for i, num in enumerate(arr):
    if num == target:
        print("The index of the target is:", i)
        break
else:
    print("Target not found in the array")

