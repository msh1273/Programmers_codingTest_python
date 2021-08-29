from typing import Sized


n = 20

def solution(n):
    answer = 0
    list = []
    for i in range(1, n+1):
        j = 0
        if(n%i == 0 and i not in list):
            j = n//i
            list.append(i)
            if(j not in list):
                list.append(j)
    return sum(list)

print(solution(n))