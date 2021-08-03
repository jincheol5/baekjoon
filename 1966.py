import sys

#해당 위치의 값이 우선순위 큐에서 몇번째로 출력될지 반환하는 함수
def find_num(q_list,dic_num,k_inq):
  count=0
  while True:
    
    if max(q_list)==q_list[0]: #중요도가 가장 높을 경우
      if k_inq==0:
        count+=1
        return count
      count+=1
      del q_list[0]
      k_inq-=1
    else: #중요도가 가장 높지 않을 경우 
      if k_inq==0:
        k_inq=len(q_list)-1
        k=q_list[0]
        del q_list[0]
        q_list.append(k) 
      else:
        k_inq-=1
        k=q_list[0]
        del q_list[0]
        q_list.append(k)
      


N=int(input())

for i in range(N):
  dic_num,k_inq=map(int,sys.stdin.readline().split()) 
  #dic_num=문서의 개수 
  #k_inq=Q 안에서 몇번째 인지,0번째가 맨 왼쪽  
  
  in_Q=list(map(int,sys.stdin.readline().split())) #중요도를 입력받아 저장한 리스트 
  print(find_num(in_Q,dic_num,k_inq))
