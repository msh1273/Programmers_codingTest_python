nums =	[3, 1, 2, 3]

# 1.배열에서 중복된걸 제외한 리스트를 만든다.
# 2.추출한 리스트에서 기회만큼 포켓몬을 챙겨간다. 
# 만약 리스트의 길이가 기회보다 작다면 가져갈 수 있는 최대 포켓몬 수는 리스트의 길이인것.
def solution(nums):
    my_set = set(nums)
    chance = len(nums)//2
    answer = 0
    if(len(my_set) < chance):
        answer = len(my_set)
    else:
        answer = chance
    return answer


print(solution(nums))