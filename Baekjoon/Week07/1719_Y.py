n, m = map(int, input().rstrip().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b, w = map(int, input().rstrip().split())
    graph[a - 1].append([b - 1, w])
    graph[b - 1].append([a - 1, w])

import heapq

answer = [[0] * n for _ in range(n)]


def dd(startPoint):
    distance = [100000000] * n
    visited =[0] * n
    queue = []
    heapq.heappush(queue, [0, startPoint])
    distance[startPoint] = 0
    visited[startPoint] = 1
    while queue:

        nowW , nowP = heapq.heappop(queue)

        for k, weight in graph[nowP]:
            newWei = nowW + weight
            if newWei < distance[k] and visited[k] == 0:
                distance[k] = newWei
                heapq.heappush(queue, [newWei, k])
                answer[k][startPoint] = nowP



    return


for i in range(n):
    dd(i)

for i in range(n):
    for j in range(n):
        if i == j:
            print("-", end=" ")
        else:
            print(answer[i][j] +1, end=" ")
    print()
