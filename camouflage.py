from typing import AnyStr


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


print(solution(clothes))