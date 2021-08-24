from sys import path_importer_cache


arr = [1]

# 첫번째 인덱스 값을 answer에 넣는다.
# 다음 값과 비교하여 같다면 넣지않고 같지않다면 추가한다.
# 예외: arr의 원소가 하나만 들어있는 경우, 2개만 들어있는경우 
def solution(arr):
    answer = []
    if (len(arr) == 1):
        answer.append(arr[0])
        return answer
    elif (len(arr) == 2):
        if(arr[0] == arr[1]):
            answer.append(arr[0])
        else:
            answer.append(arr[0])
            answer.append(arr[1])
        return answer
    else:
        for i in range(len(arr)-1):
            j = i + 1
            if(len(answer) == 0):
                answer.append(arr[0])
            if(arr[i] != arr[j]):
                answer.append(arr[j])
        return answer

# 두번째 방법 (result[-1]은 항상 배열의 마지막을 가르킨다.)
def solution1(arr):
    result = []
    for val in arr:
        if (len(result) == 0) or (result[-1] != val):
            result.append(val)
    return result

print(solution1(arr))