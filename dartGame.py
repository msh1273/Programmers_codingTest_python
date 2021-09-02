import re

dartResult = '1D2S#10S'

def solution(dartResult):
    ans = ''
    score = []
    for i in dartResult:
        if i.isnumeric():
           ans += i
        elif i == 'S':
            ans = int(ans)**1
            score.append(ans)
            ans = ''
        elif i == 'D':
            ans = int(ans)**2
            score.append(ans)
            ans = ''
        elif i == 'T':
            ans = int(ans)**3
            score.append(ans)
            ans = ''
        elif i == '*':
            if len(score) > 1:
                score[-2] = score[-2]*2
                score[-1] = score[-1]*2
            else:
                score[-1] = score[-1]*2
        elif i == '#':
            score[-1] = score[-1]*-1
    return sum(score)

print(solution(dartResult))