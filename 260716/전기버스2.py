T = int(input())
for test_case in range(1, T + 1):
    data = list(map(int, input().split()))

    N = data[0]
    battery = data[1:]

    result = float('inf')

    def dfs(current, count):
        global result

        if count >= result:
            return

        if current + battery[current] >= N - 1:
            result = min(result, count)
            return

        for next_station in range(
            current + 1,
            current + battery[current] + 1
        ):
            dfs(next_station, count + 1)

    dfs(0, 0)

    print(f'#{test_case} {result}')