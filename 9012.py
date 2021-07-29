import sys

def jud_list(s):
  a=0
  for j in range(len(s)-1):
    if s[j]=='(': a+=1
    else:
      if a==0:
        print("NO") 
        return
      else: a-=1
  if a==0: print("YES")
  else: print("NO")
  

T=int(input())


for i in range(T):
  s=sys.stdin.readline()
  jud_list(s) 
  