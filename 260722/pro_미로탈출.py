from collections import deque
def solution(maps):
    dxy = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    
    def bfs(start_x, start_y, end_x, end_y):
        queue = deque()
        queue.append((start_x, start_y, 0))

        visited = [[False] * len(maps[0]) for _ in range(len(maps))]
        visited[start_x][start_y] = True

        while queue:
            x, y, cnt = queue.popleft()

            if x == end_x and y == end_y:
                return cnt

            for dx, dy in dxy:
                nx = x + dx
                ny = y + dy

                if (0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] != 'X' and not visited[nx][ny]):
                    visited[nx][ny] = True
                    queue.append((nx, ny, cnt + 1))

        return -1

    # S, L, E 좌표 찾기
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                sx, sy = i, j
            if maps[i][j] == 'E':
                ex, ey = i, j
            if maps[i][j] == 'L':
                lx, ly = i, j

    dist1 = bfs(sx, sy, lx, ly)
    if dist1 == -1 :
        return -1
    
    dist2 = bfs(lx, ly, ex, ey)
    if dist2 == -1:
        return -1
    
    return dist1 + dist2