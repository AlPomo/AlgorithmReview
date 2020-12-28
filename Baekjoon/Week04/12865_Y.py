import sys
sys.setrecursionlimit(100000)

N, K = map(int, sys.stdin.readline().split())
knapSack = []
for _ in range(N):
    knapSack.append(list(map(int, input().rstrip().split())))
answer = -1
dp = [[0] * 100001 for _ in range(101)]


def yesOrNo(cnt, totalWeight):
    if dp[cnt][totalWeight] != 0:
        return dp[cnt][totalWeight]
    if cnt == N:
        return 0
    a = 0
    if totalWeight + knapSack[cnt][0] <= K:
        a = knapSack[cnt][1] + yesOrNo(cnt + 1, totalWeight + knapSack[cnt][0])
    b = yesOrNo(cnt + 1, totalWeight)

    dp[cnt][totalWeight] = max(a, b)

    return dp[cnt][totalWeight]


print(yesOrNo(0, 0))
