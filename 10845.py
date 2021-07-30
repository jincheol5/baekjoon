import sys

N=int(input())
Q=[]
for i in range(N):
  s=sys.stdin.readline().split()
  
  if s[0]=='push':
    Q.append(s[1])
  elif s[0]=='pop':
    if len(Q)==0: print(-1)
    else: print(Q.pop(0))
  elif s[0]=='size':
    print(len(Q))
  elif s[0]=='empty':
    if len(Q)==0: print(1)
    else: print(0)
  elif s[0]=='front':
    if len(Q)==0: print(-1)
    else: print(Q[0])
  else: #back
    if len(Q)==0: print(-1)
    else: print(Q[len(Q)-1])
