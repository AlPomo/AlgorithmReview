# 트럭들 다리 건너는 최소 시간 구하기
N, L, W = map(int,input().split()) #트럭의 수(N) , 다리의 길이(L), 다리의 하중(W)
trucks = list(map(int,input().split()))

def get_time(L, W, trucks):
    time = 0
    Q = [0] * L
    
    while Q:
        time += 1
        Q.pop(0)
        if trucks:
            if sum(Q) + trucks[0] <= W:
                temp=trucks.pop(0)
                Q.append(temp)
            else:
                Q.append(0)
    
    return time

print(get_time(L,W,trucks))