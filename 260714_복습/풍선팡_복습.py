T = int(input())
for test_case in range(1,T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    dxy = [[1,0],[0,1],[-1,0],[0,-1]]
    total_sum = 0

    for i in range(N):
        for j in range(M):
            cur = arr[i][j]

            for dx,dy in dxy:
                for k in range(1, arr[i][j] + 1):
                    nx = i + dx * k
                    ny = j + dy * k
                    if 0 <= nx < N and 0 <= ny < M:
                        cur += arr[nx][ny]
            total_sum = max(total_sum, cur)
    print(f'#{test_case} {total_sum}')