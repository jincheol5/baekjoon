import sys

def sprint(r,s):
    for i in range(len(s)):
        for j in range(r):
            print(s[i],end='')
    print()
       
T=int(input())
for i in range(T):
    ss=sys.stdin.readline().split()
    R=int(ss[0])
    
    S=ss[1]
    sprint(R,S)





