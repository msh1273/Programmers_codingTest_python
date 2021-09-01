table = [
    "SI JAVA JAVASCRIPT SQL PYTHON C#", 
"CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", 
"HARDWARE C C++ PYTHON JAVA JAVASCRIPT", 
"PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", 
"GAME C++ C# JAVASCRIPT C JAVA"
]

languages = ["JAVA", "JAVASCRIPT"]

preference = [7, 5]
# table을 2차원 배열로 만든다. (각 행의 0번째에는 직군이 있음)
# 개발자 언어 선호도를 dict타입으로 저장한다.
# 직업군 언어 점수 리스트를 생성한다.
def solution(table, languages, preference):
    answer = []
    max_ = []
    new_table = []
    dictionary = dict(zip(languages, preference))
    for idx in table:
        new_table += [idx.split()]
        
    score_table = []
    for i in range(len(new_table)):
        score_table += [makeScoreTable(new_table, i, languages)]
        
    print(score_table)
    print(preference)

    for i in range(len(score_table)):
        max_.append(innerDot(score_table[i], preference))
    max_ = max(max_)

    for i in range(len(score_table)):
        if (max_ == innerDot(score_table[i], preference)):
            answer.append(score_table[i])
    
    answer.sort()
    return answer[0][0]

def makeScoreTable(new_table, i, languages):
    score_table = []
    score_table.append(new_table[i][0])
    for key in languages:
        if key in new_table[i]:
            score_table.append(6-new_table[i].index(key))
        else:
            score_table.append(0)
    return score_table

def innerDot(a, b):
    answer = 0
    for i in range(len(b)):
        answer += a[i+1] * b[i]

    return answer
    
print(solution(table, languages, preference))
