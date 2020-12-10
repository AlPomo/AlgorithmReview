'''
토마토 문제

하나의 익은 토마토에 인접한 토마토는 그 다음날에 익는다
1. 가로,세로
2. 익은 토마토 / 안익은 토마토 / 비어있는공간

1,2가 주어졌을 때 상자안에 모든 토마토가 익는데에 걸리는 날짜를 구하라
'''

from collections import deque

def bfs(Q,arr,mem):
    row=len(arr)
    col=len(arr[0])
    
    while Q:
        r,c,d=Q.popleft()
        for dr,dc in (-1,0),(1,0),(0,1),(0,-1):
            nr=r+dr
            nc=c+dc
            if 0 <= nr < row and 0<=nc<col and arr[nr][nc]==0 and mem[nr][nc]==False:
                Q.append((nr,nc,d+1))
                mem[nr][nc]=True
    return d


if __name__ == "__main__":
    row,col = map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(col)]

    Q=deque()

    mem = [[False]*row for _ in range(col)]
    

    for r in range(col):
        for c in range(row):
            if arr[r][c]==1:
                Q.append((r,c,0))
                mem[r][c]=True
            
    ans=bfs(Q,arr,mem)
    mark=0

    for r in range(col):
        for c in range(row):
            if mem[r][c]==False and arr[r][c]==0:
                mark=-1
                print(-1)
                exit()
    if mark==0:
        print(ans)