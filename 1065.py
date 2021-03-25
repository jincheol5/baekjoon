
#리스트의 수들이 등차수열인지 판별하는 함수
def jud(a):
    if len(a)==1:
        return 1

    
    dif=a[0]-a[1]

    for i in range(len(a)-1):
        if (a[i]-a[i+1])!=dif:
            return 0
        
    return 1
              


#정수를 각 자리 숫자로 분할하는 함수  
def han(n):
    index=0
    x=[]
    while(True):
        x.append(n%10)
        index+=1
        n=(int)(n/10)
        if n<1:
            break


    return jud(x)

N=int(input())
sum=0
for i in range(N):
    if han(i+1)==1:
        sum+=1

print(sum)
