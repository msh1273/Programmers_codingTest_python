import numpy as np

def solution(a, b):
    answer = 0
    v1 = np.array(a)
    v2 = np.array(b)
    answer = np.dot(v1, v2)
    return int(answer)
