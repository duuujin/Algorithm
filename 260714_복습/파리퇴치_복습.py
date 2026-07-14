T = int(input())
for test_case in range(1,T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    total_pari = 0

    for i in range(N - M  + 1):
        for j in range(N - M + 1):
            total = 0
            for x in range(M):
                for y in range(M):
                    total += arr[i + x][j + y]
            total_pari = max(total_pari, total)
    print(f'#{test_case} {total_pari}')