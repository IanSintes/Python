n = int(input())
for _ in range(n):
    l = [int(x) for x in input().split()]

    if(l[0] == l[2] or l[1] == l[3]) or abs(l[0] - l[2]) == abs (l[1] - l[3]):
        print("SON ENEMIGAS")
    else:
        print("AMIGAS PARA SIEMPRE")