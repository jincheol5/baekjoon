



def d(n):
   
    sum=n
    while(True):
        sum=sum+(n%10)
        n=(int)(n/10)
        if n<1:
            break
    return sum



x=[]


for i in range(10000):
    x.append(d(i+1))
  
    
    
x2=[]
jud=0
for i in range(10000):
    for j in x:
        if (i+1)==j:
            jud=1
            break
    if jud==0:
        print(i+1)
    else:
        jud=0
    
               





