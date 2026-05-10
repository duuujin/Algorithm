# 백준 1926번 그림
'''
아이디어
- 2중 for , 값 1 && 방문 X => BFS
- BFS 돌면서, 그림 개수 + 1 , 최대값 갱신

시간복잡도
- BFS : O(V+E)
- V : 500 * 500
- E : 4 * 500 * 500
- V + E : 5 * 250000 => 100만 < 2억 -> 가능

자료구조
- 그래프 전체 지도 : int[][]
- 방문 여부 : bool[][]
- Queue(BFS)
'''

import sys
input = sys.stdin.readline

n,m = map(int, input().split())
maps = [list(map(int,input().split())) for _ in range(n)]
check = [[False] * m for _ in range(n)]

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def bfs(y,x) :
    rs = 1
    q = [(y,x)]
    while q :
        ey, ex = q.pop()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if  0 <= ny < n and 0 <= nx < m :
                if maps[ny][nx] == 1 and check[ny][nx] == False:
                    rs += 1
                    check[ny][nx] = True
                    q.append((ny,nx))
    return rs

cnt = 0
maxv = 0
for j in range(n):
    for i in range(m):
        if maps[j][i] == 1 and check[j][i] == False:
            check[j][i] = True
            cnt += 1
            maxv = max(maxv, bfs(j,i))

print(cnt)
print(maxv)