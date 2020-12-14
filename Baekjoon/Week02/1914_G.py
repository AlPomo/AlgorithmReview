# 하노이 탑
import sys

tray=int(sys.stdin.readline())

def hanoi(tray,start,target,other):
    if tray==1:
        print(start, target)
    else:
        hanoi(tray-1,start,other,target)
        hanoi(1,start,target,other)
        hanoi(tray-1,other,target,start)

print((2**tray)-1)
if tray <= 20:
    hanoi(tray,1,3,2)

