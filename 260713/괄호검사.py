T = int(input())
for test_case in range(1,T+1):
    s = input().strip()
    pair_dict = {
        '}' : '{',
        ')' : '(',
        ']' : '['
    }
    moeum = []
    stack = []
    for ch in s:
        if ch in pair_dict.values():
            moeum.append(ch)
        elif ch in pair_dict.keys():
            moeum.append(ch)
    
    result = 1
    for st in moeum:
        if st in pair_dict.values():
            stack.append(st)
        else:
            if not stack:
                result = 0
                break

            if stack[-1] == pair_dict[st]:
                stack.pop()
            else:
                result = 0
                break
    if stack :
        result = 0
    
    print(f'#{test_case} {result}')