n =int(input())
cList = [0] + list(map(int, input().rstrip().split()))

dp = [0] * (n + 1)
dp[1] = cList[1]
dp[2] = max(2 * cList[1], cList[2])

for i in range(3, n + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[j] + dp[i - j])

    dp[i] = max(dp[i], cList[i])

print(dp[n])