numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
hand = "right"

# 키패드
#   123
#   456
#   789
#   *0#

def solution(numbers, hand):
    answer = ''
    keypad = [[1,2,3],[4,5,6],[7,8,9],["*",0,"#"]]
    l = "*"
    r = "#"
    for num in numbers:
        num_i = 0
        num_j = 0
        left_i = 0
        left_j = 0
        right_i = 0
        right_j = 0
        
        if num == 1 or num == 4 or num == 7:
            answer += "L"
            l = num
        elif num == 3 or num == 6 or num == 9:
            answer += "R"
            r = num
        else:
            for i in range(4):
                for j in range(3):
                    if keypad[i][j] == num:
                        num_i = i
                        num_j = j
                    if keypad[i][j] == l:
                        left_i = i
                        left_j = j
                    if keypad[i][j] == r:
                        right_i = i
                        right_j = j
            leftGap = abs(num_i-left_i)+abs(num_j-left_j)
            rightGap = abs(num_i-right_i)+abs(num_j-right_j)
            
            if leftGap < rightGap:
                answer += "L"
                l = num
            elif rightGap < leftGap:
                answer += "R"
                r = num
            else:
                if hand == "right":
                    answer += "R"
                    r = num
                elif hand == "left":
                    answer += "L"
                    l = num
    return answer

print(solution(numbers, hand))