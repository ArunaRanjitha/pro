a=int(input())
li=[]
for i in range(0,a):
  b=list(map(str,input()))
  li.append(b)
c=zip(*li)
d=list(c)
for i in d:
  if(len(i)==i.count(i[0])):
    print(i[0], end='')
  else:
    break
