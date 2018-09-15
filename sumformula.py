def params(n):
    if n%2 == 0:
        return (n+1)*n//2
    elif n%2 == 1:
        return (n+2)*((n+1)//2)-n-1
    

ans = params(4)
print(ans)    
        
        