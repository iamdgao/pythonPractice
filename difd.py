def params(n):
    if n <= 17:
        return 17 - n
    else:
        return n - 17
    
def test(n):
    res = params(n)
    return res

z = test(21)
y = params(21)
print(z)
print(y)