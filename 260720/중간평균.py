T = int(input())

for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
    arr.sort()

    arr.remove(min(arr))
    arr.remove(max(arr))

    answer = int(sum(arr) / len(arr) + 0.5)

    print(f'#{test_case} {answer}')