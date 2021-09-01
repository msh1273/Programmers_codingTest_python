arr = [10, 2, 3,2]

def solution(arr):
    answer = []
    if len(arr) == 1:
        return [-1]
    else:
        arr.remove(min(arr))
    return arr

print(solution(arr))