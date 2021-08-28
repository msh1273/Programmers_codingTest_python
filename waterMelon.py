n = 3

def solution(n):
    word = '수박'
    answer = ''
    if (n%2 == 0 ):
        word *= (n//2)
    else:
        word *= (n//2)
        word = word + "수"
    return word


def solution1(n):
    word = "수박" * n
    return word[:n]
    
print(solution1(n))