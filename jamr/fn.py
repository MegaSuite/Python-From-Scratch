def f(n):
    if n==1:
        return 1
    else:
        return n*n+f(n-1)
n=int(input())
f(n)