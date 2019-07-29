x,y = map(int,input().split())
z = list(map(int,input().split()[:x]))
a = []
for i in range(y):
  i = list(map(int,input().split()))
  a.append(i)
for i in a:
  b = sum(z[i[0]-1:i[1]])
  print(b)
