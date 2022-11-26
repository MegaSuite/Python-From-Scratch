for i in range(1000,10000):
    a=i%10#个位
    b=i//100%10#百位
    c=i//1000#千位
    d=i//10%100#十位
    if (a*b==c*d)&(a+b+c+d==10):
        print(i)