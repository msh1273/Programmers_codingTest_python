n = 15

def solution(n):
    count = 0
    for i in range(1, n+1):
        _sum = 0
        for j in range(i, n+1):
            _sum += j
            if _sum == n:
                count += 1
                break
            elif _sum > n:
                break
    return count


print(solution(n))