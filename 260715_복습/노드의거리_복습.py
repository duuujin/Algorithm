from collections import deque
T = int(input())
for test_case in range(1,T+1):

    def bfs(start):
        queue = deque()
        queue.append(start)

        distance = [0] * (V + 1)
        visited = [False] * (V + 1)

        visited[start] = True
        distance[start] = 0

        while queue:
            x = queue.popleft()
            for next_node in graph[x]:
                if not visited[next_node]:
                    visited[next_node] = True
                    distance[next_node] = distance[x] + 1

                    if next_node == goal:
                        return distance[next_node]

                    queue.append(next_node)
        
        return 0


    V,E = map(int,input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        s,e = map(int,input().split())
        graph[s].append(e)
        graph[e].append(s)

    start, goal = map(int,input().split())
    result = bfs(start)
    print(f'#{test_case} {result}')