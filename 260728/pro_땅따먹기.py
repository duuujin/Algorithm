def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            best = 0

            for k in range(4):
                if k != j:
                    best = max(best, land[i - 1][k])

            land[i][j] += best

    return max(land[-1])