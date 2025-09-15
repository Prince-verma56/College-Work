# arr1 = [1, 2,3, 4, 5, 6]
# print(arr1)

list1 = [1, 2, 3, 4, 5, 6]
N = len(list1)

for i in range(0, N // 2):
    list1[i], list1[N - 1 - i] = list1[N - 1 - i], list1[i]

print(list1)