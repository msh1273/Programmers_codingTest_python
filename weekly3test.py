from collections import deque
import copy

game_board = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]

table = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]

def solution(game_board, table):
    moves = [(-1,0), (1,0), (0,-1), (0,1)]  # 상, 하, 좌, 우

    gameResult = []
    visited = [[0 for col in range(len(game_board))] for row in range(len(game_board))]
    gameResult = gamebfs(gameResult, game_board, moves, visited)

    tableResult = []
    visited = [[0 for col in range(len(table))] for row in range(len(table))]
    tableResult = tablebfs(tableResult, table, moves, visited)

    j=0
    shape = []  #정리된 게임판에 맞춰야할 퍼즐 조각
    for i in range(len(gameResult)):
        if gameResult[i] == 'SPACE':
            shape.append(gameResult[j:i])
            j = i+1

    j=0
    tableshape = [] # 정리된 테이블 퍼즐 조각
    for i in range(len(tableResult)):
        if tableResult[i] == 'SPACE':
            tableshape.append(tableResult[j:i])
            j = i+1

    formattedGameShape = []
    for i in shape:
        formattedGameShape.append(format00(i, table))

    formattedTableShape = []
    for i in tableshape:
        formattedTableShape.append(format00(i, table))

    ans = []
    gameflag = [False]*len(formattedGameShape)

    for i in range(len(formattedGameShape)):
        if formattedGameShape[i] in formattedTableShape and gameflag[i] == False:
            gameflag[i] = True
            formattedTableShape.remove(formattedGameShape[i])
            ans.append(formattedGameShape[i])
        elif gameflag[i] == False:
            tmp_shape = copy.deepcopy(formattedGameShape[i])
            for _ in range(4):
                tmp_shape = rotate90(tmp_shape,table)
                if tmp_shape in formattedTableShape and gameflag[i] == False:
                    gameflag[i] = True
                    formattedTableShape.remove(tmp_shape)
                    ans.append(formattedGameShape[i])
                    break

    fillCount = 0

    for i in ans:
        fillCount += len(i)

    return fillCount

def gamebfs(gameResult,game_board, moves, visited):
    deq = deque()
    for i in range(len(game_board)):
        for j in range(len(game_board)):
            if game_board[i][j] == 0 and visited[i][j] == 0:
                deq.append((i,j))
                visited[i][j] = 1
                while deq:
                    tx, ty = deq.popleft()
                    gameResult.append((tx,ty))
                    for mx, my in moves:
                        if 0 <= tx+mx < len(game_board) and 0 <= ty+my < len(game_board):
                            if game_board[tx+mx][ty+my] == 0 and visited[tx+mx][ty+my] == 0:
                                deq.append((tx+mx, ty+my))
                                visited[tx+mx][ty+my] = 1
                gameResult.append(('SPACE'))

    return gameResult

def tablebfs(tableResult, table, moves, visited):
    deq = deque()
    for i in range(len(table)):
        for j in range(len(table)):
            if table[i][j] == 1 and visited[i][j] == 0:
                deq.append((i,j))
                visited[i][j] = 1
                while deq:
                    tx, ty = deq.popleft()
                    tableResult.append((tx,ty))
                    for mx, my in moves:
                        if 0 <= tx+mx < len(table) and 0 <= ty+my < len(table):
                            if table[tx+mx][ty+my] == 1 and visited[tx+mx][ty+my] == 0:
                                deq.append((tx+mx, ty+my))
                                visited[tx+mx][ty+my] = 1
                tableResult.append(('SPACE'))

    return tableResult

# 도형의 시작위치를 동일하게 만들기 위한 함수
def format00(shape,table):
    temp = []
    min_x = len(table)
    min_y = len(table)
    for i in shape:
        min_x = min(min_x, i[0])
        min_y = min(min_y, i[1])

    for x, y in shape:
        temp.append((x-min_x, y-min_y))
    return sorted(temp)

# 도형을 90도씩 돌리는 경우
def rotate90(shape,table):
    temp = []
    n = len(table)
    for i in shape:
        temp.append((i[1], (n-1-i[0])))
    return sorted(format00(temp,table))

print(solution(game_board, table))