import math
n = 3

def solution(n):
    answer = int(math.sqrt(n))

    for i in range(1, int(math.sqrt(n)+1)):
        if i == math.sqrt(n):
            answer += 1
            answer = answer ** 2
            return answer
        
    return -1

print(solution(n))