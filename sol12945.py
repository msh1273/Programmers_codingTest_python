n = 5

def solution(n):
    F = []
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        F.append(0)
        F.append(1)
        for i in range(2, n+1):
            F.append((F[i-2] + F[i-1])%1234567)
        return F[-1]

print(solution(n))