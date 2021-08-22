array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def solution(array, commands):
    answer = []
    reans = []
    for i, j, k in commands:
        answer = array[i-1:j]
        answer.sort()
        reans.append(answer[k-1])
    return reans

print(solution(array, commands))