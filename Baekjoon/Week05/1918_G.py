# 후위 표기식
import sys

INPUT = sys.stdin.readline().rstrip()
STACK=[]
OPER_PRIORITY={'(':0,')':0,
                '+':1,'-':1,
                '*':2,'/':2} 

for i in '('+INPUT+')':
    if i.isalpha():
        print(i,end='')
    elif i == '(':
        STACK.append(i)
    elif i == ')':
        while True:
            k = STACK.pop()
            if k=='(':
                break
            print(k,end='')
    else:
        while STACK[-1]!='(' and OPER_PRIORITY[i] <= OPER_PRIORITY[STACK[-1]]:
            print(STACK.pop(),end='')
        STACK.append(i)
