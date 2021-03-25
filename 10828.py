#스택
#시간 줄이기 위해서 sys.stdin.readline() 활용 
import sys


def push(stack,n):
    stack.append(int(n))
def pop(stack):
    if not stack:
        print(-1)
    else:
        print(stack.pop())
def size(stack):
    print(len(stack))
def empty(stack):
    if not stack:
        print(1)
    else:
        print(0)
def top(stack):
    if not stack:
        print(-1)
    else:
        print(stack[len(stack)-1])

stack=[]

n=int(input())

for i in range(n):
    s=sys.stdin.readline().split()
    if s[0]=="push":
        push(stack,s[1])
    elif s[0]=="pop":
        pop(stack)        
    elif s[0]=="size":
        size(stack)
    elif s[0]=="empty":
        empty(stack)
    else:
        top(stack)



  
        


