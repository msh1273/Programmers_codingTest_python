from typing import AnyStr


s = "Zbcdefg"

def solution(s):
    answer = ''
    s = sorted(s, reverse=True)
    for i in s:
        answer += i
    return answer

print(solution(s))