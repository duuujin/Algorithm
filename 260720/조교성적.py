import math
T = int(input())
for test_case in range(1,T+1):
    N, K = map(int,input().split())
    total = []
    grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    for i in range(N):
        x, y, z = map(int,input().split())

        score = (x * 0.35 + y * 0.45 + z * 0.20)
        total.append(score)

        if i == K - 1:
            target = score
    
    total.sort(reverse=True)
    rank = total.index(target)
    grade_index = rank // (N // 10)
    
    print(f'#{test_case} {grades[grade_index]}')