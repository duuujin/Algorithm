T = int(input())
for test_case in range(1,T+1):
    n,m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    total_paris = 0

    for i in range(n - m + 1):
        for j in range(n - m + 1):
            total = 0
            for x in range(m):
                for y in range(m):
                    total += arr[i + x][j + y]
            total_paris = max(total_paris, total)
    print(f'#{test_case} {total_paris}')