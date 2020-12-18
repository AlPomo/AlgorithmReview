# 음식물 피하기
from collections import deque
r, c, k = map(int,input().split())
floor = [[0]*c for _ in range(r)]
check = [[False]*c for _ in range(r)]

for i in range(k):
    rt, ct = map(int,input().split())
    floor[rt-1][ct-1]=1

def bfs(i,j):
    Q = deque()
    Q.append((i,j))
    check[i][j]=True
    cnt=1
    while Q:
        x,y = Q.popleft()
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        for i in range(4):
            a_x=x+dx[i]
            a_y=y+dy[i]

            if 0<=a_x<r and 0<=a_y<c:
                if floor[a_x][a_y] == 1 and check[a_x][a_y] == False:
                    cnt+=1
                    check[a_x][a_y] = True
                    Q.append((a_x,a_y))
    return cnt

ans=0
for i in range(r):
    for j in range(c):
        if floor[i][j] == 1 and check[i][j] == False:
            ans=max(bfs(i,j),ans)
print(ans)
