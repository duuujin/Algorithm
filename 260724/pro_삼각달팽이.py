def solution(n):
    answer = []
    triangle = []
    for i in range(n):
        triangle.append([0] * (i + 1))
    
    x,y = -1, 0
    num = 1
    
    for direction in range(n):
        length = n - direction
        
        for _ in range(length):
            if direction % 3 == 0:
                x += 1
            elif direction % 3 == 1:
                y += 1
            else:
                x -= 1
                y -= 1
            
            triangle[x][y] = num
            num += 1
    
    for row in triangle:
        answer.extend(row)
    
    return answer