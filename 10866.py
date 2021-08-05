from collections import deque
import sys

N=int(input())
q=deque()
for i in range(N):
  s=list(sys.stdin.readline().split()) 
  if s[0]=='push_front':
    q.appendleft(int(s[1]))
  elif s[0]=='push_back':
    q.append(int(s[1]))
  elif s[0]=='pop_front':
    if len(q)==0: print(-1)
    else: print(q.popleft())
  elif s[0]=='pop_back':
    if len(q)==0: print(-1)
    else: print(q.pop())
  elif s[0]=='size':
    print(len(q))
  elif s[0]=='empty':
    if len(q)==0: print(1)
    else: print(0)
  elif s[0]=='front':
    if len(q)==0: print(-1)
    else:
      k=q.popleft()
      print(k)
      q.appendleft(k)
  elif s[0]=='back':
    if len(q)==0: print(-1)
    else:
      k=q.pop()
      print(k)
      q.append(k)
  else: break