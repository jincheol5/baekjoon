import sys


def left_move_q(q): #큐 왼쪽으로 한칸씩 이동시키기
  k=q[0]
  del q[0]
  q.append(k)
  return q
def right_move_q(q): #큐 오른쪽으로 한칸씩 이동시키기
  k=q[len(q)-1]
  del q[len(q)-1]
  q.insert(0,k)
  return q

  


q=[]
N,M=map(int,sys.stdin.readline().split()) 

for i in range(N): q.append(i+1) #큐 생성
k_list=list(map(int,sys.stdin.readline().split())) # 뽑을 수의 위치 리스트


count=0


while True:
  if len(k_list)==0:
    break
  k_num=k_list[0]
  if k_num==q[0]:
    del k_list[0]
    del q[0]
  else:
    count+=1
    if q.index(k_num)>len(q)/2:
      q=right_move_q(q)
    else:
      q=left_move_q(q)
    

print(count)