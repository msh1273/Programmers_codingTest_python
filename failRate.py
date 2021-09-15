N = 5
stages = [2,1,2,4,2,4,3,3]
def solution(N, stages):
    answer = []
    failRate = []
    for i in range(N):
        people = 0
        chkstage = 0
        rate = 0
        for j in stages:
            if j >= i+1:
                people += 1
                if j == i+1:
                    chkstage += 1
        if chkstage == 0 or people == 0:
            rate = 0
        else:
            rate = chkstage/people
        failRate.append((i+1, rate))

    ans = sorted(failRate, key=lambda x : (-x[1], x[0]))
    for i in ans:
        answer.append(i[0])
    return answer

print(solution(N, stages))
