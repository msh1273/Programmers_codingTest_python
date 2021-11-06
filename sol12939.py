s = "-1 -2 -3 -4"

def solution(s):
    answer = []
    s = s.split()

    for i in s:
        answer.append(int(i))
    minmax = "{} {}".format(min(answer), max(answer))
    return minmax

print(solution(s))