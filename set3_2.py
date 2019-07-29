p=int(input())
q=list(map(int,input().split()[:p]))
r=list(reversed(sorted(q)))
print(r[0]+r[1])
