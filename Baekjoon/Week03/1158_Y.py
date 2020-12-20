N, K = map(int, input().rstrip().split())
numList =[]
for i in range(N): numList.append(i+1)

s = 0
answer =[]
while len(numList) > 0:
    nextNum = (s + K - 1) % len(numList)
    answer.append(str(numList[nextNum]))
    del numList[nextNum]
    s = nextNum

print("<",', '.join(answer),">",sep='')
