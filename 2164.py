from collections import deque #데크 (양방향 큐) 사용하여 시간초과 해결 

N=int(input())
deq=deque()
for i in range(N): deq.append(i+1)
while len(deq)>1:
  deq.popleft()
  deq.append(deq.popleft())

print(deq.pop())
