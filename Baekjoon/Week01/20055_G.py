# 컨베이어벨트 내구도
import sys
from collections import deque

if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().strip().split())
    belt = deque(map(int,input().split()))
    robot=deque([0]*(2*N))
    level=0

    while True:
        level=level+1
        # 1. 벨트가 한칸 회전한다.
        belt.rotate(1)
        robot.rotate(1)
        robot[N-1]=0

        # 2. (움직일 칸 로봇없고 내구성 1 이상이면)벨트 위 로봇들이 한칸 움직인다.
        if robot[N-1]!=1:
            robot[N-1]=0
            
        for i in range(N-2,-1,-1):
            if(robot[i]!=0 and belt[i+1]>=1 and robot[i+1]==0):
                robot[i]=0
                robot[i+1]=1
                belt[i+1]=belt[i+1]-1
        robot[N-1]=0

        # 3. 올라가는 위치에 로봇 없으면 로봇이 올라간다.
        if belt[0]>0 and robot[0]==0:
            robot[0]=1
            belt[0]=belt[0]-1
        
        # 4. 내구도 0인 칸의 개수가 k개 이상이면 종료
        if belt.count(0)>=K:
            break
    print('ANSWER : ',level)
