N = int(input())

# W, S, N, E
ni = [0, -1, 1, 0]
nj = [-1, 0, 0, 1]

x, y = 0, 0
for _ in range(N):
    a, b = map(str,input().split())
    b = int(b)

    if a == 'W':
        y += ni[0] * b
        x += nj[0] * b
    
    elif a == 'S':
        y += ni[1] * b
        x += nj[1] * b

    elif a == 'N':
        y += ni[2] * b
        x += nj[2] * b

    elif a == 'E':
        y += ni[3] * b
        x += nj[3] * b

print(x,y)