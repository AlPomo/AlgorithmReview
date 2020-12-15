# 반전 요세푸스
from collections import deque

_num, _idx ,_term= map(int, input().split())

_num_list = deque()
for i in range(_num):
    _num_list.append(i+1)

_answer=[]
flag=0
p=1
while _num_list:
    flag+=1
    _num_list.rotate((-1)*(_idx-1)*p)
    if p>0:
        _answer.append(_num_list.popleft())
    else:
        _answer.append(_num_list.pop())
    
    if flag==_term:
        p=p*(-1)
        flag=0
    
    
for a in _answer:
    print(a)