N = int(input())

# W, S, N, E
ni = [0, -1, 1, 0]
nj = [-1, 0, 0, 1]

x, y = 0, 0
for _ in range(N):
    a, b = map(str,input().split())
    b = int(b)

    if a == 'W':
        for i in range(b):
            y += ni[0]
            x += nj[0]
    
    elif a == 'S':
        for i in range(b):
            y += ni[1]
            x += nj[1]

    elif a == 'N':
        for i in range(b):
            y += ni[2]
            x += nj[2]

    elif a == 'E':
        for i in range(b):
            y += ni[3]
            x += nj[3]

print(x,y)