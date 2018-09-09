def params (n):
    a = []
    for i in n:
        if i < 237 and i%2 == 0:
            a.append(i)
            
        elif i >= 237:
            break
        
    return a

y = params ([2 , 4, 7, 238, 8])
print(y)