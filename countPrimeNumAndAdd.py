left = 24
right = 27


def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if divisorCounter(i):
            answer += i
        else:
            answer -= i
    return answer

# 숫자가 들어오면 약수릐 개수가 홀수(False)개인지 짝수(True)개인지 판별하는 함수
def divisorCounter(n):
    list_ = []
    for i in range(1, n+1):
        if n%i == 0:
            list_.append(i)
    if (len(list_) % 2) == 0:
        return True
    return False

print(solution(left, right))