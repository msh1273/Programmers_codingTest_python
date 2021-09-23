numbers = [5, 0, 2, 7]

def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                _sum = numbers[i] + numbers[j]
                if _sum not in answer:
                    answer.append(_sum)
    return sorted(answer)

print(solution(numbers))