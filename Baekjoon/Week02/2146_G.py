from collections import deque
N=int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
island=1

_min=1e9

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def get_min_distance(island):
    global _min
    distance = [[-1]*N for _ in range(N)]
    q = deque()
    for y in range(N):
        for x in range(N):
            if arr[y][x] == island:
                q.append((x, y))
                distance[y][x] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if arr[ny][nx] != island and arr[ny][nx]:
                _min = min(_min, distance[y][x])
                return
            if distance[ny][nx] == -1 and not arr[ny][nx]:
                distance[ny][nx] = distance[y][x] + 1
                q.append((nx, ny))

def numbering_islands(x, y):
    arr[y][x] = island
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        visited[y][x] = 1

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if not visited[ny][nx] and arr[ny][nx]:
                arr[ny][nx] = island
                q.append((nx, ny))
                visited[ny][nx] = 1

for y in range(N):
    for x in range(N):
        if not visited[y][x] and arr[y][x]:
            numbering_islands(x, y)
            island += 1

for i in range(1, island):
    get_min_distance(i)

print(_min)