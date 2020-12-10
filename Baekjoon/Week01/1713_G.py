# 학생 후보 추천 
import sys
from collections import defaultdict

if __name__ == "__main__":
    frames=int(sys.stdin.readline())
    recommend = int(sys.stdin.readline())
    vote = list(map(int, sys.stdin.readline().strip().split()))

    recommend_cnt = defaultdict(int)
    candidate=[]

    for r in vote:
        recommend_cnt[r] += 1

        if r in candidate:
            continue
        

        if len(candidate)<frames:
            candidate.append(r)
        else:
            temp=0
            mini=1000
            for i in candidate:
                if recommend_cnt[i]<mini:
                    temp=i
                    mini=recommend_cnt[i]
            candidate.remove(temp)
            candidate.append(r)
            del(recommend_cnt[temp])

    print(*sorted(candidate))