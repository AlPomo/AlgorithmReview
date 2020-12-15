# 괄호 (스택)
# (X) : 2*X
# [X] : 3*X

import sys
_input = sys.stdin.readline()
stack=[]
val=1
ans=0

for i in range(len(_input)):
    if _input[i] == ')' or _input[i]==']':
        if len(stack)==0:
            ans=0

    if _input[i] == '(':
        stack.append('(')
        val=val*2
        if _input[i+1] == ')':
            ans += val

    elif _input[i] == '[':
        stack.append('[')
        val=val*3
        if _input[i+1] == ']':
            ans += val

    if len(stack)>0:
        if _input[i] == ')':
            val=val//2
            if stack[-1] == '(':
                stack.pop()
        elif _input[i] == ']':
            val=val//3
            if stack[-1] == '[':
                stack.pop()

if len(stack)>0:
    print(0)
else:
    print(ans)