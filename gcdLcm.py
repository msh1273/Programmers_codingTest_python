n = 3
m = 12

def solution(n, m):
    answer = []
    n_list = []
    m_list = []
    for i in range(1, n+1):
        if n % i == 0:
            n_list.append(i)
    
    for i in range(1, m+1):
        if m % i == 0:
            m_list.append(i)

    LCM = list(set(n_list) & set(m_list))
    sorted(LCM)
    GCD = n*m // LCM[-1]
    answer.append(LCM[-1])
    answer.append(GCD)
    return answer

print(solution(n,m))