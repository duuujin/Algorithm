t = int(input())
for test_case in range(1,t+1):

    def dfs(x, y):
        visited[x][y] = True
        for dx, dy in dxy:
            nx = x+dx
            ny = y+dy
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False:
                if miro[nx][ny] == 3:
                    return 1
                if miro[nx][ny] == 0:
                    if dfs(nx,ny) == 1:
                        return 1
        return 0



    N = 16
    visited = [[False] * N for _ in range(N)]
    dxy = [[0,1],[1,0],[-1,0],[0,-1]]
    miro = [list(map(int,input().strip())) for _ in range(N)]
    result = dfs(1,1)
    print(f'#{test_case} {result}')