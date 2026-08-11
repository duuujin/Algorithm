def solution(sequence, k):
    answer = []
    left = 0
    right = 0
    total = sequence[0]
    min_length = float('inf')
    
    while True:
        if total < k :
            if right == len(sequence) - 1:
                break
                
            right += 1
            total += sequence[right]
            
        elif total > k :
            total -= sequence[left]
            left += 1
            
        else:
            current_length = right - left
            
            if current_length < min_length:
                min_length = current_length
                answer = [left, right]
            
            
            total -= sequence[left]
            left += 1
    
    return answer