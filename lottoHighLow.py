lottos = [0, 0, 0, 0, 0, 0]
win_nums = [38, 19, 20, 40, 15, 25]
def solution(lottos, win_nums):
    answer = []
    count = lottos.count(0) #모르는 번호의 개수
    correct = 0
    print(count)
    for i in lottos:
        if i in win_nums:
            correct += 1
    print(correct)
    maxCorrect = count + correct
    minCorrext = correct
    answer.append(setRank(maxCorrect))
    answer.append(setRank(minCorrext))
    return answer

def setRank(correct):
    rank = 0
    if correct == 6:
        rank = 1
    elif correct == 5:
        rank = 2
    elif correct == 4:
        rank = 3
    elif correct == 3:
        rank = 4
    elif correct == 2:
        rank = 5
    else:
        rank = 6
    return rank
print(solution(lottos, win_nums))