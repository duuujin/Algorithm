T = int(input())
for test_case in range(1,T+1):
    

    def dfs(now):
        visited[now] = True
        for next_node in graph[now]:
            if next_node == goal:
                return 1
            
            if not visited[next_node]:
                if dfs(next_node) == 1:
                    return 1
        return 0


    V, E = map(int,input().split())
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        s, e = map(int,input().split())
        graph[s].append(e)

    visited = [False] * (V + 1)
    start, goal = map(int, input().split())

    result = dfs(start)
    print(f'#{test_case} {result}')
