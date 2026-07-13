T = int(input())
for test_case in range(1,T+1):
    visited = [[False] * 16 for _ in range(16)]
    def dfs(x,y):
        visited[x][y] = True

        for dx,dy in dxy:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < 16 and 0 <= ny < 16 and visited[nx][ny] == False:
                if miro[nx][ny] == 3:
                    return 1
                if miro[nx][ny] == 0:
                    if dfs(nx,ny) == 1:
                        return 1
        return 0


    n = 16
    dxy = [[0,1],[1,0],[-1,0],[0,-1]]
    miro = [list(map(int,input().strip())) for _ in range(n)]
    result = dfs(1,1)
    print(f'#{test_case} {result}')