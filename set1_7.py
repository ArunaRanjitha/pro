abc=int(input())
sum=0
for i in range(0,abc):
    if(pow(2,i)>abc):
       break
    sum=abc-pow(2,i)
print(sum)    
