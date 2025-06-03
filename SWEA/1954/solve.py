from collections import deque

dj = [1, 0, -1, 0]
di = [0, 1, 0, -1]

def dfs(i, j, d):
    if len(A) == 0:
        return
    ni = i + di[d]
    nj = j + dj[d]
    if 0 <= ni < N and 0 <= nj < N and result[ni][nj] == 0:
        result[ni][nj] = A.popleft()
        dfs(ni, nj, d)
    else:
        nd = (d + 1) % 4
        dfs(i, j, nd)

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    A = list(range(1, (N * N) + 1))
    A = deque(A)
    result = [[0 for aaaa in range(N)] for _ in range(N)]
    i = 0
    j = 0
    result[i][j] = A.popleft()
    dfs(i, j, 0)
    print(f'#{t}')
    for ii in range(N):
        print(*result[ii])
