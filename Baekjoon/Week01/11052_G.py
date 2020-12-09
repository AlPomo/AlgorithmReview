def Solution(N, price): # 
    dp=[0] * (N+1)
    p=[0]+price

    for i in range(1,N+1):
        for k in range(1,i+1):
            dp[i] = max(dp[i], dp[i-k] + p[k])

    return print(dp[N])



if __name__ == "__main__":
    N=int(input())
    price = list(map(int,input().split()))

    Solution(N,price)
    