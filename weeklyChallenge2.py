scores= [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]

def solution(scores):
    answer = ''
    student = len(scores)
    avg = []
    for j in range(student):    # j는 열 (사람)
        stu_score = []
        student = len(scores)
        for idx in range(student):    # i는 행(점수)
            stu_score.append(scores[idx][j])
        max_score = max(stu_score)
        max_count = stu_score.count(max_score)
        min_score = min(stu_score)
        min_count = stu_score.count(min_score)
        self_score = stu_score[j]
        stu_sum = sum(stu_score)
        score_count = len(stu_score)
        if(max_score == self_score and max_count == 1):
            stu_sum -= self_score
            score_count -= 1
        elif (min_score == self_score and min_count == 1):
            stu_sum -= self_score
            score_count -= 1
        
        avg.append(stu_sum / score_count) 
    return avg

def setGrade(avg):
    answer = ""
    for i in range(0, len(avg)):
        if(avg[i] >= 90):
            avg[i] = "A"
        elif(avg[i] >=80):
            avg[i] = "B"
        elif(avg[i] >=70):
            avg[i] = "C"
        elif(avg[i] >=50):
            avg[i] = "D"
        else:
            avg[i] = "F"
        answer += avg[i]
    return answer

print(setGrade(solution(scores)))