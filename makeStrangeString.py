s = "tryhelloworld"

def solution(s):
    answer = ""
    arr = s.split(' ')
    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            if(j%2==0):
                answer += arr[i][j].upper()
            else:
                answer += arr[i][j].lower()
        answer += ' '
    answer = answer[:-1]
    return answer

print(solution(s))