a,b=input().split()
a=list(a)
b=int(b)
c=a[b::]
for i in c:
    a="".join(i)
    print(a,end="")
