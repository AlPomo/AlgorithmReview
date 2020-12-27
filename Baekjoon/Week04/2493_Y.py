import sys

N = int(sys.stdin.readline())
topList = list(map(int, sys.stdin.readline().split()))
stack = []
answer = []

for i in range(N):
    nowTop = topList[i]
    while len(stack) != 0 and topList[stack[-1]] < nowTop:
        stack.pop()

    if len(stack) != 0:
        answer.append(stack[-1] + 1)
    else:
        answer.append(0)

    stack.append(i)

print(' '.join(map(str,answer)))
