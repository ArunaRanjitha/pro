x,y=map(int,input().split())
b=list(map(int,input().split()[:x]))
a=[]
for i in range(y):
  i=list(map(int,input().split()))
  a.append(i)
for i in a:
  c=min(b[i[0]-1:i[1]])
  print(c)
© 2019 GitHub, Inc.
