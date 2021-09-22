import sys


sum=0 #무게 총 합 

w_list=[] #물품 리스트
v_list=[] #물품의 가치 리스트

N,K=map(int,sys.stdin.readline().split())

for i in range(N):
  W,V=map(int,sys.stdin.readline().split())
  w_list.append(W)
  v_list.append(V)
  
