T  = int(input())
for test_case in range(1,T+1):
    money = int(input())
    type = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    result = []
    for mm in type:
        rs = money // mm
        money = money % mm
        result.append(rs)
    print(f'#{test_case}')
    print(*result)
