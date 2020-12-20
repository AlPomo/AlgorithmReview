N, K, M = map(int, input().rstrip().split())
numList = [i+1 for i in range(N)]

s = 0
# nowDirection이 1일 때 정방향 , -1일 때 역방향
nowDirection = 1
temp = 0
while len(numList) > 0:
    if nowDirection == 1:
        nextNum = (s + K - 1) % len(numList)
    else:
        nextNum = (s-K) % len(numList)
        # 파이썬의 % 음수 계산법 (파이썬은 C와 다르게 작동한다)
        # a<0 , b>0 일때 a%b의 계산법은 a가 양수가 될때까지 b를 더해준 후, 양수가 되었을 때 %실행
        # 즉, -3 % 3이라면 -3 + 3 % 3 = 0이 됨

    print(numList[nextNum])
    del numList[nextNum]
    s = nextNum
    temp += 1

    if temp == M:
        nowDirection *= -1
        temp = 0
