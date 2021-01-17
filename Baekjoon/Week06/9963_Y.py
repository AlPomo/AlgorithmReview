N = int(input())
board = [[0] * N for _ in range(N)]
answer = 0

def checkAcross(row, col, r, c):
    for i in range(len(row)):
        if abs(row[i] - r) == abs(col[i] - c):
            return False
    return True

def setQueen(i, row, col):
    global answer
    if i == N:

        answer += 1
        return
    # i가 행의 역할 j가 열을 역할
    for j in range(N):
        if i not in row and j not in col and checkAcross(row, col, i, j):
            board[i][j] = 1
            row.append(i)
            col.append(j)
            setQueen(i + 1, row , col)
            board[i][j] = 0
            col.pop()
            row.pop()

    return

r = []
c = []
setQueen(0, r, c)
print(answer)
