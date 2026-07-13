T = int(input())
for test_case in range(1,T+1):
    n, m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    dxy = [[0,1],[1,0],[-1,0],[0,-1]]
    total_sum = 0
    
    for i in range(n):
        for j in range(m):
            cur = arr[i][j]

            for dx,dy in dxy:
                for k in range(1, arr[i][j] + 1):
                    nx = i + dx * k
                    ny = j + dy * k 
                    if 0 <= nx < n and 0 <= ny < m:
                        cur += arr[nx][ny]
            total_sum = max(total_sum, cur)
    print(f'#{test_case} {total_sum}')