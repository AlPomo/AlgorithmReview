import sys
if __name__ == "__main__":
    # 숫자의 개수 m/ # 연산의 회수 n
    m,n=map(int,input().split())
    num_list = list(map(int, sys.stdin.readline().strip().split()))
    all_sum=[0]
    for i in range(m):
        all_sum.append(all_sum[i]+num_list[i])
    print("ALL_SUM : ",all_sum)

    def calculation(small,large):
        print("ALL_SUM[{}] : {}".format(large,all_sum[large]))
        print("ALL_SUM[{}] : {}".format(small,all_sum[small-1]))
        answer=all_sum[large]-all_sum[small-1]

        return print(answer)

    for k in range(n):
        small,large=map(int, sys.stdin.readline().strip().split())
        calculation(small,large)