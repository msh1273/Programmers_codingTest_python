n = 15

def solution(n):
    count = 0
    for i in range(1, n+1):
        if checkFinn(i, n):
            count += 1
    return count

def checkFinn(start, n):
    _sum = 0
    for i in range(start, n+1):
        _sum += i
        if _sum == n:
            return True
    return False

print(solution(n))