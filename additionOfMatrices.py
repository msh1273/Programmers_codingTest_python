arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]

def solution(arr1, arr2):
    answer = []
    tmp = []
    for a,b in zip(arr1,arr2):
        for c,d in zip(a, b):
            tmp.append(c+d)
        answer.append(tmp)
        tmp = []
    return answer
print(solution(arr1, arr2))