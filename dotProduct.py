import numpy as np

a = [1,2,3,4]
b = [-3,-1,0,2]

def solution(a, b):
    answer = 0
    v1 = np.array(a)
    v2 = np.array(b)
    answer = np.dot(v1, v2)
    return answer

print(solution(a,b))