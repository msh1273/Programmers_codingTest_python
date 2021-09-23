board = [
    [0,0,0,0,0],
    [0,0,1,0,3],
    [0,2,5,0,1],
    [4,2,4,4,2],
    [3,5,1,3,1]
    ]
moves = [1,5,3,5,1,2,1,4]

#한번 터질때 인형은 2개씩 사라짐.
def solution(board, moves):
    answer = []
    stack = []
    count = 0
    for i in range(len(board)):
        stack.append([a[i] for a in board])

    for i in range(len(board)):
        while 0 in stack[i]:
            stack[i].remove(0)
        stack[i].reverse()

    for i in moves:
        if len(stack[i-1]) != 0:
            answer.append(stack[i-1].pop())
            if len(answer) > 1:
                for j in range(1, len(answer)):
                    if answer[j-1] == answer[j]:
                        answer.pop()
                        answer.pop()
                        count += 1
    return count*2

print(solution(board, moves))