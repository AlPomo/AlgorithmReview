# 거북이가 지나간 영역을 포함하는 사각형의 넓이
from collections import deque
N = int(input())
_input_list=[]


for i in range(N):
    temp = input()
    _input_list.append(temp)

def get_square(_input):
    dir='up'
    direction = deque(['up','right','down','left'])

    _min_x=0
    _min_y=0
    _max_x=0
    _max_y=0

    _cur_x=0
    _cur_y=0
    for i in _input:
        if i=='L' or i=='R':
            if i == 'L':
                direction.rotate(1)
                dir=direction[0]
            elif i == 'R':
                direction.rotate(-1)
                dir=direction[0]
        else:
            if i=='F':
                val_1=1
            elif i=='B':
                val_1=-1

            if dir=='up' or dir=='right':
                val_2=1
            else:
                val_2=-1

            if dir=='up' or dir=='down':
                _cur_y=_cur_y+(val_1*val_2)
            else:
                _cur_x=_cur_x+(val_1*val_2)
        _max_x=max(_max_x,_cur_x)
        _max_y=max(_max_y,_cur_y)
        _min_x=min(_min_x,_cur_x)
        _min_y=min(_min_y,_cur_y)

        
    
    return print((_max_x-_min_x)*(_max_y-_min_y))

for _input in _input_list:
    get_square(_input)
                
        
       
    

    
