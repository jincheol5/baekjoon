import sys

T=int(input())
for i in range(T):
  s=sys.stdin.readline().strip().split(' ')
  for word in s:
    print(word[::-1],end=" ")
  
