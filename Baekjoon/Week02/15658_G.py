# 연산자 끼워넣기
import sys

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().strip().split()))
operator = list(map(int, sys.stdin.readline().strip().split()))
_max, _min = -1e9 , 1e9

def solve(idx, val) :
    global _max, _min
    if idx >= N :
        _max = max(_max, val)
        _min = min(_min, val)
        return
    if operator[0] > 0:
        operator[0] -= 1
        solve(idx+1, val+num_list[idx])
        operator[0] += 1
    if operator[1] > 0:
        operator[1] -= 1
        solve(idx+1, val-num_list[idx])
        operator[1] += 1
    if operator[2] > 0:
        operator[2] -= 1
        solve(idx+1, val*num_list[idx])
        operator[2] += 1
    if operator[3] > 0:
        operator[3] -= 1
        if val >0 :
            solve(idx+1, val//num_list[idx])
        else:
            temp= (-(val)//num_list[idx])*(-1)
            solve(idx+1,temp)
        operator[3] += 1

solve(1,num_list[0])

print(_max)
print(_min)
