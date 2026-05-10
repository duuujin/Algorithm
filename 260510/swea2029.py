T = int(input())
for test in range(1,T+1):
    n, m = map(int,input().split())
    print(f'#{test} {n // m} {n % m}')