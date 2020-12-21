#1번 풀이방벙 : Two Pointer
#구현은 투 포인터를 이용해서 했는데 왜인지.. 시간이 제일 오래 걸렸습니다.
#함께 이야기해보면 좋을 것 같아요
import sys
TC = int(sys.stdin.readline())

for _ in range(TC):
    N = int(sys.stdin.readline())
    note1 = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())  # 퀴즈의 갯수

    temp = list(map(int, sys.stdin.readline().split()))
    quizList = []
    for index, value in enumerate(temp):
        quizList.append([index, value])

    note1.sort()
    quizList = sorted(quizList, key=lambda k: k[1])

    answerList = []
    note1Pointer = 0
    for i in range(len(quizList)):

        while note1[note1Pointer] < quizList[i][1] and note1Pointer < len(note1) -1 :
            note1Pointer += 1

        if note1[note1Pointer] == quizList[i][1]:
            answerList.append([quizList[i][0], 1])
        else:
            answerList.append([quizList[i][0], 0])


    answerList = sorted(answerList, key=lambda k : k[0])
    for a, b in answerList:
        print(b)


#2번째 방법 : 간단한 방법
#52번째 라인에서 if x in List  구문은 O(n)의 복잡도를 가지고 있어서 O(n^2)이라고 생각했는데
#투포인터보다 2배정도 빨랐던 코드입니다..
import sys
input = sys.stdin.readline

TC = int(input())

for _ in range(TC):
    N = int(sys.stdin.readline())
    note1 = set(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())  # 퀴즈의 갯수
    quizList = list(map(int, sys.stdin.readline().split()))

    for quizNum in quizList:
        if quizNum in note1:
            print(1)
        else:
            print(0)

#3번째 방법 : Map을 써서 key값으로 접근 -> 런타임 오류
#이게 왜 런타임 오류인지 아직도 모르겠습니다
#같이 생각해보면 좋을것같아요! 원인을 발견하는대로 업데이트 하겠습니다.
import sys
TC = int(input())
for _ in range(TC):
    N = int(sys.stdin.readline())
    note1 = set(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())  # 퀴즈의 갯수
    quizList = list(map(int, sys.stdin.readline().split()))

    map ={}
    for ob in note1:
        if ob not in map.keys():
            map[ob] = True

    for quiz in quizList:
        if quiz not in map.keys():
            print(0)
        else:
            print(1)
