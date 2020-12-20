# 로봇
from collections import deque
row, col = map(int,input().split())
room = [[0]*col for _ in range(row)]

N_obstacle = int(input())
for _ in range(N_obstacle):
    i, j=map(int, input().split())
    room[i][j]='='

start_r, start_c = map(int,input().split())
room[start_r][start_c]=1
dirs = deque(list(map(int,input().split())))


flag=0
dx=[-1,1,0,0]
dy=[0,0,-1,1]

while True:
    if flag==4:
        room[start_r][start_c]='*'
        break
    dir=dirs[0]
    to_r=start_r+dx[dir-1]
    to_c=start_c+dy[dir-1]

    if 0<=to_r<row and 0<=to_c<col:
        if room[to_r][to_c]==0:
            flag=0
            room[to_r][to_c]=1
            start_r=to_r
            start_c=to_c
        else:
            flag+=1
            dirs.rotate(-1)
    else:
        flag+=1
        dirs.rotate(-1)

print(start_r, start_c)