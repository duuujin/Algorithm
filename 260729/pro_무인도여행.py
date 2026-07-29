from collections import deque
def solution(maps):
    dxy = [[1,0],[0,1],[-1,0],[0,-1]]
    answer = []
    row = len(maps)
    col = len(maps[0])
    visited = [[False] * col for _ in range(row)]
    
    def bfs(sx, sy):
        queue = deque()
        queue.append((sx, sy))
        visited[sx][sy] = True
        total = int(maps[sx][sy])
        
        while queue:
            x, y = queue.popleft()
            
            for dx, dy in dxy:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < row and 0 <= ny < col:
                    if visited[nx][ny] == False and maps[nx][ny] != "X":
                        visited[nx][ny] = True
                        queue.append((nx,ny))
                        total += int(maps[nx][ny]) 
                    
        return total
        
    
    for i in range(row):
        for j in range(col):
            if  maps[i][j] != "X" and visited[i][j] == False:
                land_total = bfs(i,j)
                answer.append(land_total)
                
                
    if len(answer) == 0:
        return [-1]
    
    answer.sort()
    return answer