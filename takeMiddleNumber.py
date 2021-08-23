s = "qweras"
def solution(s):
    answer = ''
    start = len(s)/2-1
    end = len(s)/2+1
    if (len(s)%2==0): #s가 짝수라면
        answer = s[start:end]
    else: 
        answer = s[start+1]
    return answer


print(solution(s))