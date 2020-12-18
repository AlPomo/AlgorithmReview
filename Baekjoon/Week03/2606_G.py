# 바이러스

from collections import deque

N = int(input())
K = int(input())
relation = [[False]*(N+1) for _ in range(N+1)]
ans=[]

for i in range(K):
    _start, _end = map(int,input().split())
    relation[_start][_end]=True
    relation[_end][_start]=True

def bfs():
    _first = 1
    Q = deque()
    Q.append(_first)
    while Q:
        x = Q.popleft()
        ans.append(x)
        for y in range(N+1):
            if (relation[x][y] or relation[y][x]) and y not in ans and y not in Q:
                Q.append(y)
    
    return len(ans)-1

print(bfs())
            