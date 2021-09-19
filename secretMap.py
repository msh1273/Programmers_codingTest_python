n = 6
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]

def solution(n, arr1, arr2):
    map_arr1 = []
    map_arr2 = []
    map_result = ["" for i in range(n)]
    for i in arr1:
        map_arr1.append(changeBinary(n, i))

    for i in arr2:
        map_arr2.append(changeBinary(n, i))

    for i in range(n):
        for j in range(n):
            if map_arr1[i][j] == 1 or map_arr2[i][j] == 1:
                map_result[i] += "#"
            else:
                map_result[i] += " "
    return map_result

def changeBinary(n, num):
    answer = []
    for i in range(n):
        answer.append(num%2)
        num = num//2
    answer.reverse()
    return answer

print(solution(n, arr1, arr2))