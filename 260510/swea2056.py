T = int(input())
for test in range(1,T+1):
    date = input()
    year = date[:4]
    month = date[4:6]
    day = date[6:]
    if int(month) > 12 or int(month) < 1:
        print(f'#{test} {-1}')
    elif int(month) == 2 and int(day) > 28 :
        print(f'#{test} {-1}')
    else :
        print(f'#{test} {year}/{month}/{day}')