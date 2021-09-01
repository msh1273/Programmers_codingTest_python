n = 12345

def solution(n):
    list_n = list(str(n))
    list_n.reverse()
    list_n = list(map(int, list_n))
    
    return list_n

# 코드라인 줄이기
def solution1(n):
    return list(map(int, reversed(str(n))))

print(solution1(n))