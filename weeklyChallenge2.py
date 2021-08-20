import numpy as np

scores= [[50,90],[50,87]]

def solution(scores):
    b= np.transpose(scores)
# 본인이 준 점수중 최고점 혹은 최저점 찾아서 0으로 만들기(단 본인이 준 최고점 혹은 최저점이 받은 점수들 가운데 중복이 있을 경우 제외하지 않음)
    def resetArray(b):
        for j in range(0, len(b)):  #j는 열
            mini = min(b[j])
            maxi = max(b[j])
            flag = True
            min_count = 0
            max_count = 0
            for i in range(0, len(b)):
                if (mini == maxi):
                    flag = False
                if(mini == b[j][i]):
                    min_count += 1
                if(maxi == b[j][i]):
                    max_count += 1
            
                if(flag and (min_count == 1 or max_count == 1) and (j == i) and ((mini == b[j][i]) or (maxi == b[j][i]))):
                    if(min_count >= 2):
                        b[j][i] = mini
                    elif(max_count >= 2):
                        b[j][i] = maxi
                    else:
                        b[j][i] = 0
        return b
    c = np.transpose(resetArray(b))   
    #학생들 수 구하기
    def countStudent(c):
        n_stu = []
        for i in range(0, len(c)):
            student = len(c)
            for j in range(0, len(c)):
                if(i == j and c[i][j] == 0):
                    student -= 1
            n_stu.append(student)
        return n_stu
    #평균 구해서 학점 주기
    def setGrade(c):
        ansarr = sum(c)/countStudent(c)
        # numpy배열 문자열 타입으로 변경
        reans = np.array(ansarr, dtype=object)
        ans = ""
        for i in range(0, len(ansarr)):
            if(ansarr[i] >= 90):
                reans[i] = "A"
            elif(ansarr[i] >=80):
                reans[i] = "B"
            elif(ansarr[i] >=70):
                reans[i] = "C"
            elif(ansarr[i] >=50):
                reans[i] = "D"
            else:
                reans[i] = "F"
            ans += reans[i]
        return ans
    

    return setGrade(c)

print(solution(scores))