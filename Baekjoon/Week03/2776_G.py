# 암기왕
# note1과 note2 비교

import sys

T = int(input())
for _ in range(T):
    N_1 = int(input())
    note_1 = set(map(int, sys.stdin.readline().strip().split()))
    N_2 = int(input())
    note_2 = list(map(int, sys.stdin.readline().strip().split()))

    for i in note_2:
        if i in note_1:
            print(1)
        else:
            print(0)
