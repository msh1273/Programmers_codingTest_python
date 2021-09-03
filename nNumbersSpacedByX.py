x = -4
n = 3

def solution(x, n):
    answer = []

    if x>0:
        for i in range(x, n*x+1, x):
            answer.append(i)
    elif x<0:
        for i in range(x, n*x-1, x):
            answer.append(i)
    elif x == 0:
        for i in range(0, n):
            answer.append(0)
    return answer

def solution1(x, n):
    return [i * x + x for i in range(n)]

print(solution1(x, n))