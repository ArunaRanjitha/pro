p=int(input())
q=list(map(int,input().split()))
r=0
for i in range(p):
    for j in range(i,p):
        for k in range(j,p):
            if(q[i]<q[j]<q[k]):
                r+=1
print(r)
