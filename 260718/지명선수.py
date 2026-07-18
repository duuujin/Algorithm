T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    a_team = list(map(int,input().split()))
    b_team = list(map(int,input().split()))

    result = [''] * (N + 1)

    a_index = 0
    b_index = 0
    picked = 0

    while picked < N :
        while result[a_team[a_index]] != '':
            a_index += 1
        
        player = a_team[a_index]
        result[player] = 'A'
        a_index += 1
        picked += 1

        if picked == N :
            break

        while result[b_team[b_index]] != '':
            b_index += 1
        
        player = b_team[b_index]
        result[player] = 'B'
        b_index += 1
        picked += 1

    print("".join(result[1:]))