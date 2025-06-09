def A(n, m):
    if m >= M:
        while m > M:
            n = n / N
            m -= 1
        return n
     
    n = n * N 
    return A(n, m + 1)
 
for t in range(1, 11):
    tc = input()
    N, M = map(int, input().split())
    result = A(N, 1)  
     
    print(f'#{t} {result}')