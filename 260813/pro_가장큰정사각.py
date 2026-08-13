def solution(board):
    answer = 0
    
    row = len(board)
    col = len(board[0])
    
    for i in range(row):
        for j in range(col):
            if board[i][j] == 1:
                answer = 1
    
    for i in range(1,row):
        for j in range(1,col):
            if board[i][j] == 1: 
                board[i][j] = min(board[i][j-1], board[i-1][j], board[i-1][j-1]) + 1
                answer = max(answer, board[i][j])
    
    

    return answer ** 2