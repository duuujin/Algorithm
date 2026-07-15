T = int(input())
for test_case in range(1,T+1):
    N = int(input().strip())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [False] * N
    result = float('inf')

    def dfs(now, count, total):
        global result
        if total >= result:
            return
        
        if count == N:
            result = min(result, total+arr[now][0])
            return
        
        for next_node in range(1,N):
            if not visited[next_node]:
                visited[next_node] = True
                dfs(next_node, count + 1, total + arr[now][next_node])
                visited[next_node] = False

    visited[0] = True
    dfs(0,1,0)
    print(f'#{test_case} {result}')