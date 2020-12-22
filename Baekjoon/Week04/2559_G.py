# 수열
import sys
N, K = map(int,sys.stdin.readline().split())
Temp = list(map(int,sys.stdin.readline().split()))

cur=sum(Temp[0:K])
cur_max=cur
i=0
while i+K<N:
    plus=Temp[K+i]
    minus=Temp[i]
    cur=cur+plus-minus

    cur_max=max(cur_max,cur)
    i+=1
print(cur_max)
