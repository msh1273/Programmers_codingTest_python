from math import gcd
arr = [2,6,8,14]

def solution(arr):
    answer = arr[0]
    for i in range(1, len(arr)):
        answer = (answer*arr[i]) // gcd(answer, arr[i])
    return answer

print(solution(arr))