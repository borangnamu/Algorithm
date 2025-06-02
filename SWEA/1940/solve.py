

import sys
sys.stdin = open('a.txt', 'r')
sys.stdout = open('c.txt', 'w')


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    result = 0
    acc = 0
    for _ in range(N):
        Cab = list(map(int, input().split()))
        if len(Cab) == 2:
            Ca, Cb = Cab[0], Cab[1]
            if Ca == 1:
                acc += Cb
            elif Ca == 2:
                if acc != 0:
                    acc -= Cb

        if acc > 0:
            result += acc


    print(f'#{t} {result}')

