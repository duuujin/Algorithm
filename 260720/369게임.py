N = int(input())
arr = []
for i in range(1, N+1):
    word = str(i)
    cnt = word.count("3") + word.count("6") + word.count("9")
    if cnt > 0:
        arr.append('-' * cnt)
    else:
        arr.append(word)
print(*arr)
