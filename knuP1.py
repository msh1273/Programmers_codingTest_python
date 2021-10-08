from enum import Flag
import re
s= "aabb"

def  solution(s):
    ans = []
    list_s = list(s)
    queue = []
    queue.append(list_s[0])
    for i in range(1, len(list_s)):
        if len(queue) < 2:
            if list_s[i] == queue[-1]:
                queue.append(list_s[i])
                if i == len(list_s)-1:
                    ans.append("".join(queue))
                    ans.append("|")
            else:
                queue.pop(0)
                queue.append(list_s[i])
        else:
            if list_s[i] == queue[-1]:
                queue.append(list_s[i])
                if i == len(list_s)-1:
                    ans.append("".join(queue))
                    ans.append("|")
            else:
                ans.append("".join(queue))
                ans.append("|")
                queue = []
                queue.append(list_s[i])
    answer = "".join(ans)
    answer = answer[:-1]
    p1 = re.split(answer, s)
    print(ans)
    return p1

print(solution(s))