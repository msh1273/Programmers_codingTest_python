n = 123

def solution(n):
    str_n = list(str(n))
    list_n = list(map(int, str_n))

    return sum(list_n)

print(solution(n))