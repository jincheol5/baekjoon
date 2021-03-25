def solve(a):
    ans=0
    for x in a:
        ans+=a
    return ans
    
    
a=[]
n=int(input())

for i in range(n):
    a.append(int(input()))

print(solve(a))