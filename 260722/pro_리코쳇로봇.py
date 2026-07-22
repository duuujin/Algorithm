from collections import deque
dxy = [[1,0],[0,1],[-1,0],[0,-1]]
def solution(board):
    visited = [[False] * len(board[0]) for _ in range(len(board))]
    queue = deque()
    
    # R 값의 좌표 찾기
    find = False
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                visited[i][j] = True
                queue.append((i,j,0))
                find = True
                break
        if find :
            break
    
    # BFS 돌리기
    while queue:
        x,y,cnt = queue.popleft()
        
        if board[x][y] == 'G':
            return cnt
        
        for dx, dy in dxy:
            nx = x
            ny = y
            while (0 <= nx + dx < len(board) and 0 <= ny + dy < len(board[0]) and board[nx + dx][ny + dy] != 'D' ):
                nx += dx
                ny += dy
            if not visited[nx][ny] :
                visited[nx][ny] = True
                queue.append((nx,ny,cnt+1))
                    
    
    return -1