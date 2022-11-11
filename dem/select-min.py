def select_min(a,b,c):
    temp=a[b:c]
    return min(temp)
min = select_min([11,33,22], 1, 3)
print(min) 