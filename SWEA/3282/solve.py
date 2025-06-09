def D(n, weight):
    if n >= N:
        return 0
     
    if (n, weight) in memo:
        return memo[(n, weight)]
     
    result = D(n + 1, weight)
     
    if weight + A[n][0] <= K:
        result = max(result, D(n + 1, weight + A[n][0]) + A[n][1])
     
    memo[(n, weight)] = result
    return result
 
T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    A = []
    memo = {}
     
    for _ in range(N):
        V, C = map(int, input().split())
        A.append((V, C))
     
    result = D(0, 0)
    print(f'#{t} {result}')