# 수들의 합
S=int(input())
N=0
while True:
    if (N*(N+1))//2 > S:
        N-=1
        break
    else:
        N+=1

print(N)