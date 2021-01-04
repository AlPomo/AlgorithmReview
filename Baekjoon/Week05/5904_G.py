# Moo 게임

N = int(input())
idx=3
k=4
while True:
    idx = 2*idx + k
    k+=1
    if idx > N:
        break
k-=1

while True:
    temp = (idx-k)//2
    if N<=temp:
        k=k-1
        idx=temp
    elif N>temp+k:
        N = N-(temp+k)
        k=k-1
        idx=temp
    else:
        N=N-temp
        break

if N==1:
    print('m')
else:
    print('o')