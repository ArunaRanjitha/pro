a,b=map(int,input().split())
p=list(map(int,input().split()[:a]))
q=[]
for i in range(b):
  i=list(map(int,input().split()))
  q.append(i)
for i in q:
  c = p[i[0]-1:i[1]]
  d = c[0]
  for j in range(len(c) - 1):
    d = d ^ c[j + 1]
  print(d)
