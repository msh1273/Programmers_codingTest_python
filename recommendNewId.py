import re

new_id = "=.="
def solution(new_id):
    answer = ''
    #1단계
    new_id = new_id.lower()
    #2단계
    for i in new_id:
        if i.isdigit() or i.islower() or i == "-" or i == "_" or i == ".":
            answer += i
    #3단계
    answer = re.sub("[..]+", ".", answer)
    #4단계
    if len(answer) == 1 and answer[0] == ".":
        answer = answer[1:]
    if (len(answer) >= 2 and answer[0] == "."):
        answer = answer[1:]
    if (len(answer) >= 2 and answer[-1] == "."):
        answer = answer[:-1]
    #5단계
    if len(answer) == 0:
        answer += "a"
    #6단계
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[len(answer)-1] == ".":
            answer = answer[:-1]
    #7단계
    if len(answer) == 1:
        answer += answer[-1]*2
    elif len(answer) == 2:
        answer += answer[-1]
    return answer

print(solution(new_id))