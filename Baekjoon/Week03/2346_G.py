# 풍선 터뜨리기
import sys
from collections import deque

N = int(input())
val_balloon=deque(list(map(int,sys.stdin.readline().strip().split())))

num_balloon=deque()
for i in range(N):
    num_balloon.append(i+1)

answer=[]
while val_balloon:
    print('-'*40)
    print("NUM BALLOON : ",num_balloon)
    print("VAL BALLOON : ",val_balloon)

    move_idx=val_balloon.popleft()
    answer.append(num_balloon.popleft())
    if len(num_balloon)!=0:
        if move_idx>0:
            move_idx-= int(move_idx//len(num_balloon))+1
        elif move_idx<0:
            move_idx+= int(move_idx//len(num_balloon))+1
    

    print("MOVE_IDX : ",move_idx)

    num_balloon.rotate(-1*(move_idx))
    val_balloon.rotate(-1*(move_idx))


_string=''
for ans in answer:
    _string=_string+str(ans)+' '

print(_string)

    