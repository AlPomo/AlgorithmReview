N = int(input())
totalStrLen = 3
k = 0
while N > totalStrLen:
    totalStrLen = 2 * totalStrLen + k+4
    k += 1
k += 3

def dfs(strLen, k, N):
    x = int((strLen - k) / 2)
    if x < N <= x + k:
        N -= x
        if N == 1:
            print('m')
        else:
            print('o')
        return

    if x >= N:
        dfs(x, k - 1, N)
    else:
        dfs(x, k - 1, N - (x + k))

dfs(totalStrLen, k, N)
