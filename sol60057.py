s = "aabbaccc"

def solution(s):
    answer = []
    if len(s) == 1:
        return 1
    else:
        for i in range(1, len(s)):    #몇 글자씩 자를 것인가
            answer.append(cutString(i, s))
        answer.sort()
        return answer[0]

# n개 단위로 잘랐을때 문자열의 길이를 리턴하는 함수
def cutString(n, s):
    result = []
    j = 0
    for i in range(n, len(s)+n, n):
        result.append(s[j:i])
        j += n
        
    k = 1
    count = 1
    c_list = []
    for i in range(0, len(result)-1):
        if result[i] == result[k]:
            count += 1
        else:
            c_list.append(count)
            count = 1
        if i == len(result)-2:
            c_list.append(count)
        k += 1

    print("c_list:", c_list)

    ansList = []
    ansList.append(result[0])
    for i in range(1, len(result)):
        if ansList[-1] != result[i]:
            ansList.append(result[i])

    fullAns = []
    for i in range(len(ansList)):
        if c_list[i] != 1:
            fullAns.append(str(c_list[i])+ansList[i])
        elif c_list[i] == 1:
            fullAns.append(ansList[i])

    answer = "".join(fullAns)
    print("ansList:", ansList)
    print(answer)
    return len(answer)

print(cutString(2, s))