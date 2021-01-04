# 천재 수학자 성필
INPUT= input()
stack=[]
for i in INPUT:
    if i =='+':
        pop2=stack.pop()
        pop1=stack.pop()
        stack.append(pop1+pop2)
    elif i =='-':
        pop2=stack.pop()
        pop1=stack.pop()
        stack.append(pop1-pop2)
    elif i =='*':
        pop2=stack.pop()
        pop1=stack.pop()
        stack.append(pop1*pop2)
    elif i =='/':
        pop2=stack.pop()
        pop1=stack.pop()
        if pop1%pop2==0:
            stack.append(int(pop1/pop2))
        else:
            stack.append(pop1/pop2)
    else:
        stack.append(int(i))
print(stack[0])

