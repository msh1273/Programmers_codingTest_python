from collections import Counter

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

#의상 종류별로 리스트를 정리한다.
# ex) {'headgear': ['yellowhat', 'green_turban'], 'eyewear': ['bluesunglasses']}

def solution(clothes):
    type = {}
    answer = 1
    for key, value in clothes:
        if value in type:
            type[value].append(key)
        else:
            type[value] = [key]
    
    for key in type.keys():
        answer *= (len(type[key]) + 1)
    return answer-1

# 추가) Counter를 사용한 풀이
def solution1(clothes):
    answer = 1 
    c = Counter(key[1] for key in clothes) #clothes의 종류별 갯수를 dic 형태로 변환
    
    for i in c.values():
        answer *= i+1
    answer -= 1
    return answer


print(solution1(clothes))