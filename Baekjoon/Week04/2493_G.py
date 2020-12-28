# 탑
import sys
from collections import deque
N = int(input())
Towers = list(map(int, sys.stdin.readline().split()))

Answer=deque()

def find(tower,Towers,N):
    meet_idx=0
    for i in range(N,-1,-1):
        if Towers[i]>tower :
            meet_idx=i+1
            break
    return meet_idx

temp_N=N
while Towers:
    tower = Towers.pop()
    temp_N-=1
    meet_idx=find(tower,Towers,temp_N-1)
    Answer.appendleft(meet_idx)

for i in range(N):
    if i == N-1:
        print(Answer[i])
    else:
        print(Answer[i],end=" ")


################################################################
N = int(input())
stack=[]
Answer=[]
for i,idx in enumerate(map(int, input().split()),1):
    while True:
        if not stack:
            Answer.append(0)
            stack.append((idx,i))
            break
        else:
            if stack[-1][0] < idx:
                stack.pop()
            else:
                Answer.append(stack[-1][1])
                stack.append((idx,i))
                break

for k in Answer:
    print(k,end=" ")