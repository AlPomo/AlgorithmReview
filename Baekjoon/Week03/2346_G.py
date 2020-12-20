# 풍선 터뜨리기
import sys
from collections import deque

N = int(input())
val_balloon=deque(list(map(int,sys.stdin.readline().strip().split())))

num_balloon=deque()
for i in range(N):
    num_balloon.append(i+1)

answer=[]
move_idx=0
while val_balloon:
    if move_idx<0:
        move_idx=val_balloon.pop()
        answer.append(num_balloon.pop())
    else:
        move_idx=val_balloon.popleft()
        answer.append(num_balloon.popleft())

    if move_idx<0:
        num_balloon.rotate(-1*(move_idx+1))
        val_balloon.rotate(-1*(move_idx+1))
    elif move_idx>0:
        num_balloon.rotate(-1*(move_idx-1))
        val_balloon.rotate(-1*(move_idx-1))

_string=''
for ans in answer:
    _string=_string+str(ans)+' '

print(_string)

    