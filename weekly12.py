from itertools import permutations

k = 80  #현재 피로도
dungeons = [[80,10]]    # 0: 최소 피로도 1: 소모 피로도

def solution(k, dungeons):
    countlist = []
    allCase = list(permutations(dungeons, len(dungeons)))

    for i in allCase:
        k=80
        count = 0
        for need, use in i:
            if k >= need and k >=use:   #던전을 돌 피로도가 남아있고 소모피로도도 남아있음
                k -= use
                count += 1
            else:
                break
        countlist.append(count)

    return max(countlist)

print(solution(k, dungeons))
