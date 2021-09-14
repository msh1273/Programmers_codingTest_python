weights = [50,82,75,120]
head2head = ["NLWL","WNLL","LWNW","WWLN"]	

#weights = 몸무게, head2head = 전적
def solution(weights, head2head):
    winCount = []   # i+1번 선수가 자기보다 무거운 복서를 몇 번 이겼나
    answer = []
    for i in range(len(head2head)):
        overWin = 0
        win = 0
        stage = 0
        for j in range(len(head2head)):
            if head2head[i][j] == 'W' or head2head[i][j] == 'L':
                stage += 1
                if head2head[i][j] == 'W':
                    win += 1
                    if weights[i] < weights[j]:
                        overWin += 1
        if stage != 0:
            winper = win/stage*100
        else:
            winper = 0
        winCount.append((i+1, winper, overWin, weights[i]))
    ans = sorted(winCount, key=lambda x : (-x[1], -x[2], -x[3]))
    
    for i in ans:
        answer.append(i[0])

    return answer

print(solution(weights, head2head))