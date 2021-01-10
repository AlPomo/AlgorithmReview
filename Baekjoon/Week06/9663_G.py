# N-Queen
import sys
N = int(sys.stdin.readline()) 

def DFS(i):
    global N, COL, RIGHT_UP, RIGHT_DOWN, ans

    if i==N:
        ans+=1
        return

    for j in range(N):
        if not (COL[j] or RIGHT_UP[i+j] or RIGHT_DOWN[i-j+N-1]):
            COL[j] = RIGHT_UP[i+j] = RIGHT_DOWN[i-j+N-1] = True
            DFS(i+1)
            COL[j] = RIGHT_UP[i+j] = RIGHT_DOWN[i-j+N-1] = False

COL, RIGHT_UP, RIGHT_DOWN = [False] * N, [False] * (2*N-1), [False] * (2*N-1)
ans=0
DFS(0)
 
print(ans)