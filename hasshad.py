arr = 234

def solution(x):
    divide = sum(map(int, str(x)))
    print(divide)
    if x%divide == 0:
        return True
    return False

print(solution(arr))