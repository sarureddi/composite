r1=int(input())
fl1=0
for i in range(2,r1-1):
    if(r1%i==0):
        fl1=1 
if(fl1==1):
    print("yes")
else:
    print("no")
