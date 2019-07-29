n = int(input())
a= []
e= []
for i in range(2**n):
    b = bin(i)[2:]
    l = len(b)
    b = str(0) * (n - l) + b
    a.append(b)
for i in a:
    c = i.count("1")
    d = (c,i)
    e.append(d)
for i in sorted(e):
    print(i[1])
