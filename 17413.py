from collections import deque

S=input()
result=''
q=deque()
stack=[]
jud=False #false = 스택,true = 큐 에 저장 
for i in S:
  if i=='<':
    while stack:
      result+=stack.pop()
    jud=True
  if i=='>':
    q.append(i)
    while q:
      result+=q.popleft()
    jud=False
    continue
  if i==' ' and jud==False:
    while stack:
      result+=stack.pop()
    result+=' '
    continue

  if jud:
    q.append(i)
  else:
    stack.append(i)

#뒤에 나머지 스택 있으면 추가 
while stack:
  result+=stack.pop()

print(result)