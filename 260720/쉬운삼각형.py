T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    points = []

    for _ in range(N):
        x, y = map(int, input().split())
        points.append((x, y))

    answer = 0

    for i in range(N):
        for j in range(N):
            for k in range(N):
                x1, y1 = points[i]
                x2, y2 = points[j]
                x3, y3 = points[k]

                if y1 == y2 and x1 == x3:
                    width = abs(x1 - x2)
                    height = abs(y1 - y3)

                    area = width * height
                    answer = max(answer, area)

    print(answer)