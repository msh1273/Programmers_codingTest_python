n = 125

def solution(n):
    answer = 0
    a = []
    while n != 0:
        a.append(n%3)
        n = n//3

    j = 0
    for i in range(len(a)-1, -1, -1):
        print(i)
        answer += a[j]*(3**i)
        j += 1
    return answer

print(solution(n))