#[::-1] 문자열 거꾸로 

s=input().split()
a=s[0]
b=s[1]
s1=int(a[::-1])
s2=int(b[::-1])

if s1>s2: print(s1)
else: print(s2)
