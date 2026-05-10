T = int(input())
for test in range(1, T+1):
    a,b = map(int,input().split())
    if a < b :
        print(f'#{test} {"<"}')
    elif a == b :
        print(f'#{test} {"="}')
    else :
        print(f'#{test} {">"}')