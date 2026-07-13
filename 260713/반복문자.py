T = int(input())
for test_case in range(1,T+1):
    s = input().strip()
    answer = []
    for ch in s:
        if answer and ch == answer[-1]:
            answer.pop()
        else:
            answer.append(ch)

    print(f'#{test_case} {len(answer)}')