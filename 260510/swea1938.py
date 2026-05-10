n, m = map(int,input().split())
for i in range(4):
    if i == 0 :
        print(n + m)
    elif i == 1 :
        print(n - m)
    elif i == 2 :
        print(n * m)
    else :
        print(n // m)