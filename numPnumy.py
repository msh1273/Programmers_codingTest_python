s = "Pyy"

def solution(s):
    pnum = s.count('p') + s.count("P")
    ynum = s.count('y') + s.count('Y')
    if pnum == ynum:
        return True
    else:
        return False

print(solution(s))