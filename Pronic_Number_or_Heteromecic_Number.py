n=int(input())
c=0
for i in range(1,n):
    if(i*(i+1)==n):
        c=c+1
if(c==0):
    print("NO")
else:
    print("YES")