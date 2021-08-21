absolutes = [1, 2, 3]
signs = [False, False, True]

def solution(absolutes, signs):
    sum = 0
    for i in range(len(absolutes)):
        if (signs[i] == False):
            sum -= absolutes[i]
        else:
            sum += absolutes[i]
    
    return sum

solution(absolutes, signs)