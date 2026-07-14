t = int(input())
for test_case in range(1,t+1):
    s = input().strip()
    check = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }
    moeum = []
    for ch in s:
        if ch in check.values():
            moeum.append(ch)
        if ch in check.keys():
            moeum.append(ch)

    stack = []
    result = 1
    for st in moeum:
        if st in check.values():
            stack.append(st)
        else:
            if not stack:
                result = 0
                break

            if stack[-1] == check[st]:
                stack.pop()
            else:
                result = 0
                break
    if stack:
        result = 0
    
    print(f'#{test_case} {result}')
