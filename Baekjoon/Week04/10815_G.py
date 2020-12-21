#숫자 카드
import sys
N=int(input())
N_list = list(map(int, sys.stdin.readline().strip().split()))

M=int(input())
M_list=list(map(int, sys.stdin.readline().strip().split()))

N_list.sort()


for i in M_list:
    MIN, MAX = 0, len(N_list)
    while True:
        if MIN > MAX:
            MAX = MAX+1
            break
        mid = (MIN+MAX)//2
        if 0 <= mid < len(N_list):
            if N_list[mid] < i:
                MIN = mid+1
            else:
                MAX = mid-1
        else:
            break
    if 0 <= MAX < len(N_list):
        if N_list[MAX]==i:
            print(1,end=" ")
        else:
            print(0,end=" ")
    else:
        print(0,end=" ")