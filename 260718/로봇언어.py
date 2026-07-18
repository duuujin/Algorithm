T = int(input())
for test_case in range(1,T+1):
    s = input().strip()
    cnt = 0
    question = 0
    answer = 0

    for ch in s:
        if ch ==  'L' :
            cnt -= 1
            
        elif ch == 'R':
            cnt += 1

        else:
            question += 1
        
        distance = max(abs(cnt - question), abs(cnt + question))

        answer = max(distance, answer)
    print(answer)