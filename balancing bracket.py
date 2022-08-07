def arepairs(open,close):
    if open=='['  and close==']':
        return True
    if open=='{' and close=='}':
        return True
    if open=='(' and close==')':
        return True

def balance(a):
    stack=[]
    for i in range(len(a)):
        if a[i]=='[' or a[i]=='{' or a[i]=='(':
            stack.append(a[i])
        elif a[i]==']' or a[i]=='}' or a[i]==')':
            if arepairs(stack[-1],a[i] or len(stack) ):
                stack.pop()
            else:
                return False
    if len(stack)==0:
        return True
    else:
        return False

a="[(a+b)-(([a+b)]"
print(balance(a))
    
