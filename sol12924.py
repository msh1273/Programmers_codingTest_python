n = 15

# def solution(n):
#     count = 0
#     for i in range(1, n+1):
#         _sum = 0
#         for j in range(i, n+1):
#             _sum += j
#             if _sum == n:
#                 count += 1
#                 break
#             elif _sum > n:
#                 break
#     return count

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
        elif _sum > n:
            break
    return False

print(solution(n))