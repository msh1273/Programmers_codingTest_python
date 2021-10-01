from itertools import permutations

numbers = "17"
def solution(numbers):
    answer = []
    allCase = []
    numbers = list(numbers)
    for i in range(1 , len(numbers)+1):
        allCase = list(map(''.join ,permutations(numbers, i)))
        for j in set(allCase):
            if primeNumber(int(j)) and int(j) not in answer:
                answer.append(int(j))
    return len(answer)

def primeNumber(n):
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if n%i == 0:
                return False
        return True

print(solution(numbers))
print(primeNumber(17))