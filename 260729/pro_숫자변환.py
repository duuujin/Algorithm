from collections import deque

def solution(x, y, n):
    queue = deque()
    queue.append((x,0))
    
    visited = set()
    visited.add(x)
    
    while queue:
        current, cnt = queue.popleft()
        
        if current == y :
            return cnt
        
        next_current = [current + n , current * 2, current * 3]
        
        for next_num in next_current :
            if next_num <= y and next_num not in visited:
                visited.add(next_num)
                queue.append((next_num, cnt + 1))
        
    return -1