s = "a B z"
n = 4

def solution(s, n):
    answer = ''
    for i in s:
        if i.isupper():
            i = chr(ord(i)+n)
            if ord(i)>90:
                answer += chr(64 + ord(i)-90)
            else:
                answer += i
        elif i.islower():
            i = chr(ord(i)+n)
            if ord(i)>122:
                answer += chr(96 + ord(i)-122)
            else:
                answer += i
        elif i == " ":
            answer += " "

    return answer

print(solution(s, n))