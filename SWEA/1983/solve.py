G = ['D0', 'C-', 'C0', 'C+', 'B-', 'B0', 'B+', 'A-', 'A0', 'A+']
T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    NN = N // 10
    Grade = []
    for i in range(N):
        A, B, C = map(int, input().split())
        A = A * 0.35
        B = B * 0.45
        C = C * 0.20
        H = A + B + C
        Grade.append((H, i))
    Grade.sort()
    for i in range(N):
        if Grade[i][1] == K - 1:
            C = i // NN
            print(f'#{t} {G[C]}')
            break