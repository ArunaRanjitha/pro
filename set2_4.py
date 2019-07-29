x,y=map(int,input().split())
a=list(map(int,input().split()[:x]))
b=[]
for i in range(y):
  i=list(map(int,input().split()))
  b.append(i)
for i in b:
  c = a[i[0]-1:i[1]]
  d = c[0]
  for j in range(len(c) - 1):
    d = d ^ c[j + 1]
  print(d)
