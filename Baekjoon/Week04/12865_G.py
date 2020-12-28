# 평범한 배낭
N, K = map(int, input().split()) 
dp=[[0 for _ in range(K+1)] for _ in range(N+1)]

weight = [0]
value = [0]

for _ in range(N):
    W, V = map(int,input().split())
    weight.append(W)
    value.append(V)


## 이 부분 잘 모르겠어서 dp 풀이 참고 좀 했당ㅠㅠ 다시 풀어봐야게써,,
for n in range(1,N+1):
    for k in range(1,K+1):
        if k-weight[n] >= 0:
            dp[n][k] = max(dp[n-1][k], value[n]+dp[n-1][k-weight[n]])
        else:
            dp[n][k] = dp[n-1][k]

print(max(dp[n]))