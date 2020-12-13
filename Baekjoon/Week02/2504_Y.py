s = input()
sList = list(s)
stack = []

for i in sList:
    if i == ']':
        summary = 0
        while stack:
            temp = stack.pop()
            if temp == '[':
                if summary == 0:
                    stack.append(3)
                else:
                    stack.append(summary*3)
                break
            elif temp == '(':
                print(0)
                exit(0)
            else:
                summary += int(temp)
    elif i == ')':
        summary = 0
        while stack:
            temp = stack.pop()
            if temp == '(':
                if summary == 0:
                    stack.append(2)
                else:
                    stack.append(summary*2)
                break
            elif temp == '[':
                print(0)
                exit(0)
            else:
                summary += int(temp)
    else:
        stack.append(i)


answer = 0
for i in stack:
    if i == '(' or i == ')' or i == '[' or i == ']':
        print(0)
        exit(0)
    else:
        answer += i

print(answer)
