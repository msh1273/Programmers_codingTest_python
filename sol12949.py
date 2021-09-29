import numpy as np

arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 3], [3, 3]]
def solution(arr1, arr2):
    answer = [[]]
    a1 = np.array(arr1)
    a2 = np.array(arr2)
    answer = a1.dot(a2)
    return answer.tolist()

def solution1(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        answer.append([])
        for j in range(len(arr2[0])):
            sum = 0
            for k in range(len(arr1[0])):
                sum += arr1[i][k] * arr2[k][j]
            answer[i].append(sum)
    return answer

def productMatrix(A, B):
    answer = []
    c = 0
    for i in A:
        answer.append([])
        for j in zip(*B):
            sum = 0
            for a,b in zip(i,j):
                sum += a*b
            answer[c].append(sum)
        c = c + 1
    print(answer)
print(productMatrix(arr1, arr2))