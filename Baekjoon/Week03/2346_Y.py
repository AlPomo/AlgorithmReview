N = int(input())
bList = list(map(int, input().rstrip().split()))
boom = [0] * len(bList)

def checkIdx(index, num):
    print(index + 1, end=' ')
    if num > 0:
        while num > 0:
            index += 1
            if index > N - 1: index = 0

            if boom[index] == 0:
                num -= 1
    else:
        while num < 0:
            index -= 1
            if index < 0: index = N - 1

            if boom[index] == 0:
                num += 1
    boom[index] = 1

    return index


def dfs(idx, number):
    if 0 not in boom:
        print(idx + 1)
        return
    nextIdx = checkIdx(idx, number)
    dfs(nextIdx, bList[nextIdx])


boom[0] = 1
dfs(0, bList[0])
