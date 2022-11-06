def Combinatorial(n, m):
    Min = min(m,n-m)
    result = 1
    for i in range(0, Min):
        result = result * (n-i) / (Min-i)
    return result

    
Combinatorial(5,3)