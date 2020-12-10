# 팰린드롬 만들기(앞으로 읽어도, 뒤에서 읽어도 같은 문자열)

_input = input()
def palindrome(_input):
    _alphabet = dict()
    odd = []

    for i in _input:
        if i not in _alphabet:
            _alphabet[i]=1
        else:
            _alphabet[i]+=1
    start=[]
    for key,val in _alphabet.items():
        if val%2==1:
            odd.append(key)

        if len(odd)>1:
            return print("I'm Sorry Hansoo")

        for i in range(int(val/2)):
            start.append(key)

    start.sort()
    end=list(reversed(start))
    
    ans=""
    for r in start+odd+end:
        ans=ans+r
    return print(ans)
palindrome(_input)


    

