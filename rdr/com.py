def combNumber(m, n, b):
    for i in range(m, n-1, -1):   
        b[n-1] = i
        if n-1>0:
            combNumber(i-1,n-1,b)
        else:
            print (b)
            
group=[0,0,0]
combNumber(5,3,group)