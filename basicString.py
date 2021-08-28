s = "1234"

def solution(s):
    answer = False
    if ((len(s) == 4 or len(s) == 6) and s.isdigit()):
        return True
    return answer

print(solution(s))