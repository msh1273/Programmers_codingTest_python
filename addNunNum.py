numbers = [5,8,4,0,6,7,9]
def solution(numbers):
    answer = 0
    for i in range(10):
        if i not in numbers:
            answer += i
    return answer

print(solution(numbers))