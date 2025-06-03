T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N - M + 1):
        for j in range(N -  M + 1):
            sumA = 0
            for ij in range(M):
                sumA += sum(A[i+ij][j:j+M])
            result = max(sumA, result)

    print(f'#{t} {result}')