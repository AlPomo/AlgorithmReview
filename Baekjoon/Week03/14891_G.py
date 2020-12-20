# 톱니바퀴
import sys
from collections import deque

gear_list = []
for _ in range(4):
    gear=deque(list(sys.stdin.readline().replace("\n","")))  
    gear_list.append(gear)

N = int(input())
idx_dir = deque()
for i in range(N):
    gear_idx, dir = map(int, input().split())
    idx_dir.append((gear_idx-1,dir))

def get_point(gear_list):
    point=0
    if gear_list[0][0]=='1':
        point+=1
    if gear_list[1][0]=='1':
        point+=2
    if gear_list[2][0]=='1':
        point+=4
    if gear_list[3][0]=='1':
        point+=8
    return point

def check_right(gear_idx, dir):
    if gear_idx > 3 or gear_list[gear_idx-1][2] == gear_list[gear_idx][6]:
        return

    if gear_list[gear_idx-1][2] != gear_list[gear_idx][6]:
        check_right(gear_idx+1, -dir)
        gear_list[gear_idx].rotate(dir)


def check_left(gear_idx, dir):
    if gear_idx < 0 or gear_list[gear_idx+1][6] == gear_list[gear_idx][2]:
        return

    if gear_list[gear_idx+1][6] != gear_list[gear_idx][2]:
        check_left(gear_idx-1, -dir)
        gear_list[gear_idx].rotate(dir)

def rotate_gear(gear_list,idx_dir):
    while idx_dir:
        gear_idx, dir = idx_dir.popleft()
        check_left(gear_idx-1,-dir)
        check_right(gear_idx+1, -dir)
        gear_list[gear_idx].rotate(dir)

    return gear_list

rotate_gear(gear_list,idx_dir)
print(get_point(gear_list))