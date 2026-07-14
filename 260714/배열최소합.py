T = int(input())
for test_case in range(1,T+1):
    result = float('inf')
    def dfs(row, total):
        global result 
        if total >= result:
            return

        if row == N :
            result = min(result , total)
            return
        
        for col in range(N):
            if not visited[col]:
                visited[col] = True
                dfs(row + 1, total + arr[row][col])
                visited[col] = False


    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [False] * N

    dfs(0,0)

    print(f'#{test_case} {result}')