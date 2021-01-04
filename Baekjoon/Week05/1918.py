m = input()

stack = []
answer = []
for i in m:

    if i.isupper():
        answer.append(i)
    elif i == '(':
        stack.append(i)
    elif i == ')':
        while True:
            x = stack.pop()
            if x == '(':
                break
            answer.append(x)
    else:
        if i == '+' or i == '-':
            while True:
                if len(stack) >0:
                    x = stack.pop()
                    if x == '(':
                        stack.append(x)
                        stack.append(i)
                        break
                    else:
                        answer.append(x)
                else:
                    stack.append(i)
                    break
        elif i == '*' or i == '/':
            while True:
                if len(stack) > 0:
                    x = stack.pop()
                    if x == '(':
                        stack.append(x)
                        stack.append(i)
                        break
                    elif x == '*' or x == '/':
                        answer.append(x)
                    else:
                        stack.append(x)
                        stack.append(i)
                        break
                else:
                    stack.append(i)
                    break

stack.reverse()
print(''.join(answer + stack))
