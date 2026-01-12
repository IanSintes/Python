import math
n = int(input())
for i in range(n):
    s = input()
    x = s.split()
    c = math.pow(int(x[0]),2)+ math.pow(int(x[1]),2)
    print(math.ceil(math.sqrt(c)))