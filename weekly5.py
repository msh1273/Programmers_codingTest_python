from itertools import product, repeat

word = "AAAAE"
def solution(word):
    dic = 'AEIOU'
    result = []
    for i in range(1, 6):
        result += list(map(''.join, product(dic, repeat=i)))
    
    result.sort()

    answer = result.index(word)+1
    return answer

print(solution(word))