import numpy as np

arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
def solution(arr1, arr2):
    answer = [[]]
    a1 = np.array(arr1)
    a2 = np.array(arr2)
    answer = a1.dot(a2)
    return answer.tolist()

print(solution(arr1, arr2))