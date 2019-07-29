n1 = int(input())
a1= []
e1= []
for i in range(2**n1):
    b1 = bin(i)[2:]
    l = len(b1)
    b1 = str(0) * (n1 - l) + b1
    a1.append(b1)
for i in a1:
    c = i.count("1")
    d = (c,i)
    e1.append(d)
for i in sorted(e1):
    print(i[1])
