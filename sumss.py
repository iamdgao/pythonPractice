def params(a,b,c):
    if a==b==c:
        return 3*(a+b+c)
    else:
        return a+b+c
    
res = params(3, 3, 3)
print(res)