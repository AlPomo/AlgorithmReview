#잃어버린 괄호
import sys

STRING = list(map(str,sys.stdin.readline().rstrip().split('-')))

ans=0

for i in STRING[0].split('+'):
    ans+=int(i)

for i in STRING[1:]:
    for j in i.split('+'):
        ans -= int(j)

print(ans)