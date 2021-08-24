n = 3
lost = [3]
reserve = [1]

# 1.lost배열과 reserve배열에 같은 학생이 있는경우 두 배열에서 제거한다. (여벌옷이 있지만 도난당한 학생)

def solution(n, lost, reserve):
    # 두 리스트의 서로 중복되는 부분 제거
    setLost = list(set(lost) - set(reserve))
    setReserve = list(set(reserve) - set(lost))
    for i in setReserve:
            if (i-1 in setLost):
                setLost.remove(i-1)
            elif (i+1 in setLost):
                setLost.remove(i+1)
    return n - len(setLost)

print(solution(n, lost, reserve))