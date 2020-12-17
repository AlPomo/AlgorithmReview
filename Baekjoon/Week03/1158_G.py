# 요세푸스 문제
from collections import deque
_num, _idx = map(int, input().split())

_num_list = deque()
for i in range(_num):
    _num_list.append(i+1)

_answer=[]
while _num_list:
    _num_list.rotate((-1)*(_idx-1))
    _answer.append(str(_num_list.popleft()))

print("<",", ".join(_answer)[:],">", sep='')