import math


def solution(progresses, speeds):
    deploy = []
    for i in range(len(progresses)):
        n = math.ceil((100 - progresses[i])/speeds[i])
        deploy.append(n)
    start = deploy[0]
    answer = []
    count = 0
    print(deploy)
    for i in range(len(deploy)):
        if deploy[i] <= start:
            count += 1
            if i == len(deploy)-1:
                answer.append(count)
        else:
            start = deploy[i]
            answer.append(count)
            count = 1
            if i == len(deploy)-1:
                answer.append(count)

    return answer
