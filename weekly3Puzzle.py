from collections import deque

game_board = [
    [1,1,0,0,1,0],
    [0,0,1,0,1,0],
    [0,1,1,0,0,1],
    [1,1,0,1,1,1],
    [1,0,0,0,1,0],
    [0,1,1,1,0,0]
    ]

table = [
    [1,0,0,1,1,0],
    [1,0,1,0,1,0],
    [0,1,1,0,1,1],
    [0,0,1,0,0,0],
    [1,1,0,1,1,0],
    [0,1,0,0,0,0]
    ]

moves = [(-1,0), (1,0), (0,-1), (0,1)]  # 상, 하, 좌, 우
def solution(game_board, table):
    answer = -1
    return answer

visited = [[0 for col in range(6)] for row in range(6)]
gameResult = []
def gamebfs(game_board, moves):
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
                        if 0 <= tx+mx < 6 and 0 <= ty+my < 6:
                            if game_board[tx+mx][ty+my] == 0 and visited[tx+mx][ty+my] == 0:
                                deq.append((tx+mx, ty+my))
                                visited[tx+mx][ty+my] = 1
                gameResult.append(('SPACE'))

    return gameResult

tableResult = []
def tablebfs(table, moves):
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
                        if 0 <= tx+mx < 6 and 0 <= ty+my < 6:
                            if table[tx+mx][ty+my] == 1 and visited[tx+mx][ty+my] == 0:
                                deq.append((tx+mx, ty+my))
                                visited[tx+mx][ty+my] = 1
                tableResult.append(('SPACE'))

    return tableResult

gamebfs(game_board, moves)
visited = [[0 for col in range(6)] for row in range(6)]
tablebfs(table, moves)

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

# 도형의 시작위치를 0,0으로 만들기 위한 함수
def format00(shape):
    temp = []
    tmp_x = shape[0][0]
    tmp_y = shape[0][1]
    for x, y in shape:
        temp.append((x-tmp_x, y-tmp_y))
    return sorted(temp)

formattedGameShape = []
for i in shape:
    formattedGameShape.append(format00(i))

formattedTableShape = []
for i in tableshape:
    formattedTableShape.append(format00(i))


# 도형을 90도씩 돌리는 경우
def rotate90(shape):
    rotate = [[0, 1], [-1,0]]
    temp = []
    for i in shape:
        temp.append([i[0]*rotate[0][0] + i[1] * rotate[0][1], i[0]*rotate[1][0]+i[1]*rotate[1][1]])
    return temp

print('보드에 맞춰야 하는 퍼즐', formattedGameShape)
print(formattedTableShape)

count = 0
for i in formattedTableShape:
    for j in formattedTableShape:
        if i == j:
            formattedTableShape.pop()
