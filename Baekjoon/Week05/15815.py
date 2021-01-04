s = list(input())

stack = []
for i in s:
    if i in '0123456789':
        stack.append(int(i))
    else:
        a = stack.pop()
        b = stack.pop()
        if i == '*':
            stack.append(b * a)
        elif i == '+':
            stack.append(b + a)
        elif i == '-':
            stack.append(b - a)
        else:
            stack.append(int(b/a))

print(stack[0])
