n = 8
a = 1
b = 2

def solution(n,a,b):
    answer = 0
    while a!=b:
        a = (a+1)//2
        b = (b+1)//2
        answer += 1
        print(answer)
    return answer

print(solution(n,a,b))