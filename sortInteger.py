n = 118372

def solution(n):
    answer = ''
    str_n = list(str(n))
    str_n.sort(reverse=True)

    for i in str_n:
        answer += i

    return int(answer)

solution(n)