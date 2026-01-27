def ArreglarPalabra(s):
    res = ""
    i = 0
    while i < len(s):
        if s[i:i+4].lower() == "amol":
            res += s[i:i+4]
            i += 4
        else:
            char = s[i]
            if char == "L": res += "R"
            elif char == "l": res += "r"
            elif char == "R": res += "L"
            elif char == "r": res += "l"
            else: res += char
            i += 1
    return res

def ArreglarLista(a):
    res = []
    for e in a:
        res.append(ArreglarPalabra(e))
    return res

try:
    linea = input()
    if linea:
        n = int(linea)
        for _ in range(n):
            a = input().split()
            s = ArreglarLista(a)
            print(" ".join(s))
except EOFError:
    pass


"""
def Canvi(s):
    x=""
    for e in s:
        if e=="L":
            x +="R"
        elif e=="l":
            x +="r" 
        elif e=="R":
            x +="L"
        elif e=="r":
            x +="l"
        else:
            x += e
    return x
def DurAmor(s):
    a = s.lower()
    if "amol" ==a:
         return s
    elif "amol" in a:
        p=0
        prefix=""
        postfix=""
        while a[p]!="a":
            p+=1
        if p>0:
            prefix = Canvi(s[:p])
        while a[p]!="o":
            p+=1
        p+=1
        if p<len(s):
            postfix=Canvi(s[p:])
        return prefix+"amol"+postfix
    else:
        return s
def Areglar(a):
    s=[]
    for e in a:
        s.append(DurAmor(e))
    return Canvi(s)

n = int(input())
for _ in range(n):
    a = input().split()
    s = Areglar(a)
    print(" ".join(s))
"""