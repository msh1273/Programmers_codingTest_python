numbers = [0,0,0,0]

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x : x*3 ,reverse=True)
    answer = ''.join(numbers)
    answer = str(int(answer))
    return type(answer)

print(solution(numbers))