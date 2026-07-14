from collections import deque
t = int(input())
for test_case in range(1,t+1):

    def bfs(arr):
        queue = deque()
        queue.append((1,1))
        visited = [[False] * N for _ in range(N)]
        visited[1][1] = True
        
        while queue:
            x, y = queue.popleft()
            for dx, dy in dxy:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False and (arr[nx][ny] == 0 or arr[nx][ny] == 3):
                    if arr[nx][ny] == 3:
                        return 1
                    queue.append((nx,ny))
                    visited[nx][ny] = True
        return 0





    N = 16
    miro = [list(map(int,input().strip())) for _ in range(N)]
    dxy = [[0,1],[1,0],[-1,0],[0,-1]]
    result = bfs(miro)
    print(f'#{test_case} {result}')