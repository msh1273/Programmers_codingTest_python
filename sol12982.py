d = [2,2,3,3]
budget = 10

def solution(d, budget):
    answer = 0
    d.sort()
    _sum = 0
    for i in d:
        _sum += i
        if _sum <= budget:
            answer += 1
    return answer

print(solution(d, budget))