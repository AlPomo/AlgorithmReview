from collections import deque
N = int(input())
board = []
for i in range(N):
    board.append(list(map(int, input().rstrip().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
outLine = []
answer = 999999
def bfs(i, j, index):
    queue = deque()
    queue.append([i, j])
    board[i][j] = index

    while len(queue) > 0:
        nowX, nowY = queue.popleft()
        bl = False
        for k in range(4):
            nextX = nowX + dx[k]
            nextY = nowY + dy[k]
            if 0 <= nextX < N and 0 <= nextY < N:
                if board[nextX][nextY] == 1:
                    queue.append([nextX, nextY])
                    board[nextX][nextY] = index
                elif board[nextX][nextY] == 0:
                    bl = True

        if bl:
            outLine.append([nowX, nowY, index])
    return

landIndex = 1
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            landIndex += 1
            bfs(i, j, landIndex)

for x1,y1,landIndex1 in outLine:
    for x2,y2,landIndex2 in outLine:
        if x1 == x2 and y1 == y2:
            continue
        if landIndex1 != landIndex2:
            answer = min(answer , abs(x1 - x2) + abs(y1 -y2) -1)


print(answer)
