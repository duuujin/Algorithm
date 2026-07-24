from itertools import permutations
def solution(numbers):
    answer = 0
    nums = set()
    
    # 순열 생성
    for lenth in range(1,len(numbers) + 1):
        for p in permutations(numbers, lenth):
            num = int(''.join(p))
            nums.add(num)
    
    for num in nums:
        if num < 2:
            continue
            
        is_prime = True
        
        # 소수 판별
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        
        if is_prime :
            answer += 1
    
    return answer 