# 랜선 자르기
import sys
K, N = map(int, sys.stdin.readline().split())
LANS=[]
for _ in range(K):
    length = int(sys.stdin.readline())
    LANS.append(length)

MIN, MAX = 1, max(LANS)

while True:
    if MIN>MAX:
        break
    ans=0
    mid = (MIN+MAX)//2
    for i in LANS:
        ans+=i//mid

    if ans >= N:
        MIN=mid+1
    else:
        MAX=mid-1

print(MAX)
