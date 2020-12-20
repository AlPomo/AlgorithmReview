# 분기를 N번째 톱니, N 이전의 톱니, N 이후의 톱니로 나눈 코드입니다.
# 공통된 코드가 있어서 좋은 코드는 아닌것같아요.🤣
from collections import deque

gearList = []
for _ in range(4):
    gearList.append(deque(list(input().rstrip())))

for _ in range(int(input())):
    tempList = []
    N, D = map(int, input().rstrip().split())

    # N번째 톱니
    if D == 1:
        tempList.append([N - 1, 1])
        D = -1
    else:
        tempList.append([N - 1, -1])
        D = 1
    initDirection = D

    # N번째 톱니로부터 왼쪽
    s = N - 2
    while s > -1:
        interSide = gearList[s][2]
        if gearList[s + 1][6] != interSide:
            if D == 1:
                tempList.append([s, 1])
                D = -1
            else:
                tempList.append([s, -1])
                D = 1
        else:
            break

        s -= 1

    D = initDirection
    # N번쨰 톱니로부터 오른쪽
    s = N
    while s < 4:
        interSide = gearList[s][6]
        if gearList[s - 1][2] != interSide:
            if D == 1:
                tempList.append([s, 1])
                D = -1
            else:
                tempList.append([s, -1])
                D = 1
        else:
            break
        s += 1

    for s, clockWise in tempList:
        if clockWise == 1:
            gearList[s].rotate(1)
        else:
            gearList[s].rotate(-1)

answer = 0
temp = [1, 2, 4, 8]
for index, value in enumerate(gearList):
    answer += (int(value[0]) * temp[index])

print(answer)
