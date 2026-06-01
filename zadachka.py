import numpy as np
import random


def analyses(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1):
            n1 = arr[i, j]
            n2 = arr[i + 1, j]
            n3 = arr[i, j + 1]
            n4 = arr[i + 1, j + 1]
            if n1 == n2 == n3 or n2 == n3 == n4 or n3 == n4 == n1:
                return True
    return False


arr = np.array([random.choices(['P', 'W'], k=3) for _ in range(3)])

# arr = np.array([[1, 1, 1], [0, 0, 0], [1, 1, 1]])
print(arr)
print(analyses(arr))

# l = [[1, 2], [3, 4]]
# # print(l[0][0], l[0][1])
# # print(l[1])
# l = [[1, 2], [3, 4]]
# for i in range(len(l)):
#     print(l[i])
#     for j in range(len(l[i])):
#         print(l[i][j])
